import logging
import logging
import math
import time
import traceback
from typing import Dict, Optional

from binance.client import Client
from binance.exceptions import BinanceAPIException
from cachetools import TTLCache, cached

from src.binance_stream_manager import BinanceCache, \
    BinanceOrder, BinanceStreamManager, OrderGuard
from src.config import Config
from src.database import Database
from src.models import Coin

_logger = logging.getLogger(__name__)


class BinanceAPIManager:
    def __init__(self, config: Config, db: Database):
        # initializing the client class calls `ping`
        # API endpoint, verifying the connection
        self.binance_client = Client(
            config.BINANCE_API_KEY,
            config.BINANCE_API_SECRET_KEY,
            tld=config.BINANCE_TLD,
        )
        self.db = db
        self.config = config

        self.cache = BinanceCache()
        self.stream_manager: Optional[BinanceStreamManager] = None
        self.setup_websockets()

    def setup_websockets(self):
        self.stream_manager = BinanceStreamManager(
            self.cache,
            self.config,
            self.binance_client,
        )

    @cached(cache=TTLCache(maxsize=1, ttl=43200))
    def get_trade_fees(self) -> Dict[str, float]:
        return {
            ticker["symbol"]: float(ticker["takerCommission"])
            for ticker in self.binance_client.get_trade_fee()
        }

    @cached(cache=TTLCache(maxsize=1, ttl=60))
    def get_using_bnb_for_fees(self):
        return self.binance_client.get_bnb_burn_spot_margin()["spotBNBBurn"]

    def get_fee(self, origin_coin: Coin, target_coin: Coin, selling: bool,
                limit_balance=None):
        base_fee = self.get_trade_fees()[origin_coin + target_coin]
        if not self.get_using_bnb_for_fees():
            return base_fee

        # The discount is only applied if we have enough BNB to cover the fee
        amount_trading = (
            self._sell_quantity(origin_coin.symbol, target_coin.symbol)
            if selling
            else self._buy_quantity(origin_coin.symbol, target_coin.symbol,
                                    limit_balance)
        )

        fee_amount = amount_trading * base_fee * 0.75
        if origin_coin.symbol == "BNB":
            fee_amount_bnb = fee_amount
        else:
            origin_price = self.get_ticker_price(origin_coin + Coin("BNB"))
            if origin_price is None:
                return base_fee
            fee_amount_bnb = fee_amount * origin_price

        bnb_balance = self.get_currency_balance("BNB")

        if bnb_balance >= fee_amount_bnb:
            return base_fee * 0.75
        return base_fee

    def get_account(self):
        """
        Get account information
        """
        return self.binance_client.get_account()

    def get_ticker_price(self, ticker_symbol: str):
        """
        Get ticker price of a specific coin
        """
        price = self.cache.ticker_values.get(ticker_symbol, None)
        if price is None and ticker_symbol \
                not in self.cache.non_existent_tickers:
            self.cache.ticker_values = {
                ticker["symbol"]: float(ticker["price"]) for ticker in
                self.binance_client.get_symbol_ticker()
            }
            _logger.debug(
                f"Fetched all ticker prices: {self.cache.ticker_values}")
            price = self.cache.ticker_values.get(ticker_symbol, None)
            if price is None:
                _logger.info(
                    f"Ticker does not exist: {ticker_symbol}"
                    f" - will not be fetched from now on")
                self.cache.non_existent_tickers.add(ticker_symbol)

        return price

    def get_currency_balance(self, currency_symbol: str, force=False) -> float:
        """
        Get balance of a specific coin
        """
        with self.cache.open_balances() as cache_balances:
            balance = cache_balances.get(currency_symbol, None)
            if force or balance is None:
                cache_balances.clear()
                cache_balances.update(
                    {
                        currency_balance["asset"]: float(
                            currency_balance["free"])
                        for currency_balance in
                        self.binance_client.get_account()["balances"]
                    }
                )
                _logger.debug(f"Fetched all balances: {cache_balances}")
                if currency_symbol not in cache_balances:
                    cache_balances[currency_symbol] = 0.0
                    return 0.0
                return cache_balances.get(currency_symbol, 0.0)

            return balance

    def get_balance(self):
        """
        return latest balance
        :return:
        """
        resp = self.binance_client.get_account()["balances"]
        return {
            currency_balance["asset"]: float(currency_balance["free"]) for
            currency_balance in resp if
            float(currency_balance["free"]) > 0.0 and
            currency_balance['asset'] not in self.config.IGNORE_COINS
        }

    @staticmethod
    def retry(func, *args, **kwargs):
        for attempt in range(20):
            # noinspection PyBroadException
            try:
                return func(*args, **kwargs)
            except Exception:  # pylint: disable=broad-except
                _logger.warning(
                    f"Failed to Buy/Sell. Trying Again (attempt {attempt}/20)")
                if attempt == 0:
                    _logger.warning(traceback.format_exc())
                time.sleep(1)
        return None

    def get_symbol_filter(self, origin_symbol: str, target_symbol: str,
                          filter_type: str):
        return next(
            _filter
            for _filter in
            self.binance_client.get_symbol_info(origin_symbol + target_symbol)[
                "filters"]
            if _filter["filterType"] == filter_type
        )

    @cached(cache=TTLCache(maxsize=2000, ttl=43200))
    def get_alt_tick(self, origin_symbol: str, target_symbol: str):
        step_size = \
            self.get_symbol_filter(origin_symbol, target_symbol, "LOT_SIZE")[
                "stepSize"]
        if step_size.find("1") == 0:
            return 1 - step_size.find(".")
        return step_size.find("1") - 1

    @cached(cache=TTLCache(maxsize=2000, ttl=43200))
    def get_min_notional(self, origin_symbol: str, target_symbol: str):
        return float(self.get_symbol_filter(origin_symbol, target_symbol,
                                            "MIN_NOTIONAL")["minNotional"])

    @cached(cache=TTLCache(maxsize=2000, ttl=3600))
    def get_top_alt_gainer24hr(self, topn=10):
        """
        Get top gainer altcoin in 24h
        :param topn:
        :return:
        """
        bridge = self.config.BRIDGE.symbol
        resp = self.binance_client.get_ticker()
        ticker_statistic = sorted(
            resp, key=lambda item: (
                float(item['priceChangePercent']), float(item['volume'])),
            reverse=True
        )
        alt_coin_bridge_gainer = [{
            item['symbol'][:len(item['symbol']) - len(bridge)],
        } for item in ticker_statistic if item['symbol'].endswith(bridge)]

        return alt_coin_bridge_gainer[:topn]

    def get_all_symbol(self):
        """
        Get all symbol [C98,DOGE, BTC,...]
        :return:
        """
        resp = self.binance_client.get_exchange_info()
        symbols = [item['baseAsset'] for item in resp['symbols']]
        return list(dict.fromkeys(symbols))

    def _wait_for_order(
            self, order_id, origin_symbol: str, target_symbol: str
    ) -> Optional[BinanceOrder]:  # pylint: disable=unsubscriptable-object
        while True:
            order_status: BinanceOrder = self.cache.orders.get(order_id, None)
            if order_status is not None:
                break
            _logger.debug(f"Waiting for order {order_id} to be created")
            time.sleep(1)

        _logger.debug(f"Order created: {order_status}")

        while order_status.status != "FILLED":
            try:
                order_status = self.cache.orders.get(order_id, None)

                _logger.debug(f"Waiting for order {order_id} to be filled")

                if self._should_cancel_order(order_status):
                    cancel_order = None
                    while cancel_order is None:
                        cancel_order = self.binance_client.cancel_order(
                            symbol=origin_symbol + target_symbol,
                            orderId=order_id
                        )
                    _logger.info("Order timeout, canceled...")

                    # sell partially
                    if order_status.status == "PARTIALLY_FILLED" \
                            and order_status.side == "BUY":
                        _logger.info("Sell partially filled amount")

                        order_quantity = self._sell_quantity(origin_symbol,
                                                             target_symbol)
                        partially_order = None
                        while partially_order is None:
                            partially_order = self.binance_client.order_market_sell(
                                symbol=origin_symbol + target_symbol,
                                quantity=order_quantity
                            )

                    _logger.info("Going back to scouting mode...")
                    return None

                if order_status.status == "CANCELED":
                    _logger.info(
                        "Order is canceled, going back to scouting mode...")
                    return None

                time.sleep(1)
            except BinanceAPIException as e:
                _logger.info(e)
                time.sleep(1)
            except Exception as e:  # pylint: disable=broad-except
                _logger.info(f"Unexpected Error: {e}")
                time.sleep(1)

        _logger.debug(f"Order filled: {order_status}")
        return order_status

    def wait_for_order(
            self, order_id, origin_symbol: str, target_symbol: str,
            order_guard: OrderGuard
    ) -> Optional[BinanceOrder]:  # pylint: disable=unsubscriptable-object
        with order_guard:
            return self._wait_for_order(order_id, origin_symbol, target_symbol)

    def _should_cancel_order(self, order_status):
        minutes = (time.time() - order_status.time / 1000) / 60

        if order_status.side == "SELL":
            timeout = float(self.config.SELL_TIMEOUT)
        else:
            timeout = float(self.config.BUY_TIMEOUT)

        if timeout and minutes > timeout and order_status.status == "NEW":
            return True

        if timeout and minutes > timeout and \
                order_status.status == "PARTIALLY_FILLED":
            if order_status.side == "SELL":
                return True

            if order_status.side == "BUY":
                current_price = self.get_ticker_price(order_status.symbol)
                if float(current_price) * (1 - 0.001) > float(
                        order_status.price):
                    return True

        return False

    def buy_alt(self, origin_coin: Coin, target_coin: Coin,
                limit_balance: float = None) -> BinanceOrder:
        return self.retry(
            self._buy_alt, origin_coin, target_coin, limit_balance
        )

    def _buy_quantity(
            self, origin_symbol: str, target_symbol: str,
            target_balance: float = None, from_coin_price: float = None
    ):
        target_balance = target_balance or self.get_currency_balance(
            target_symbol)
        from_coin_price = from_coin_price or self.get_ticker_price(
            origin_symbol + target_symbol)

        origin_tick = self.get_alt_tick(origin_symbol, target_symbol)
        return math.floor(
            target_balance * 10 ** origin_tick / from_coin_price) / float(
            10 ** origin_tick)

    def _buy_alt(self, origin_coin: Coin, target_coin: Coin,
                 limit_balance=None):
        """
        Buy altcoin
        """
        trade_log = self.db.start_trade_log(origin_coin, target_coin, False)
        origin_symbol = origin_coin.symbol
        target_symbol = target_coin.symbol

        with self.cache.open_balances() as balances:
            balances.clear()

        origin_balance = self.get_currency_balance(origin_symbol)
        target_balance = self.get_currency_balance(target_symbol)
        pair_info = self.binance_client.get_symbol_info(
            origin_symbol + target_symbol
        )
        from_coin_price = self.get_ticker_price(origin_symbol + target_symbol)
        from_coin_price_s = "{:0.0{}f}".format(from_coin_price,
                                               pair_info["quotePrecision"])

        order_quantity = self._buy_quantity(
            origin_symbol, target_symbol, limit_balance, from_coin_price
        )
        if limit_balance:
            order_quantity = self._buy_quantity(
                origin_symbol, target_symbol, limit_balance, from_coin_price
            )

        order_quantity_s = "{:0.0{}f}".format(order_quantity,
                                              pair_info["baseAssetPrecision"])

        _logger.info(f"BUY QUANTITY {order_quantity}")

        # Try to buy until successful
        order = None
        order_guard = self.stream_manager.acquire_order_guard()
        transaction_fee = 0
        while order is None:
            try:
                order = self.binance_client.order_limit_buy(
                    symbol=origin_symbol + target_symbol,
                    quantity=order_quantity_s,
                    price=from_coin_price_s,
                )
                _logger.info(order)
                _logger.info("transaction fee: %s", transaction_fee)
                transaction_fee = self.get_fee(origin_coin, target_coin,
                                               selling=False)
            except BinanceAPIException as e:
                _logger.info(e)
                time.sleep(1)
            except Exception as e:  # pylint: disable=broad-except
                _logger.warning(f"Unexpected Error: {e}")

        trade_log.set_ordered(origin_balance, target_balance, order_quantity,
                              transaction_fee)

        order_guard.set_order(origin_symbol, target_symbol,
                              int(order["orderId"]))
        order = self.wait_for_order(order["orderId"], origin_symbol,
                                    target_symbol, order_guard)

        if order is None:
            return None

        _logger.info(f"Bought {origin_symbol}")

        trade_log.set_complete(order.cumulative_quote_qty)

        return order

    def sell_alt(self, origin_coin: Coin, target_coin: Coin) -> BinanceOrder:
        return self.retry(self._sell_alt, origin_coin, target_coin)

    def _sell_quantity(self, origin_symbol: str, target_symbol: str,
                       origin_balance: float = None):
        origin_balance = origin_balance or self.get_currency_balance(
            origin_symbol)

        origin_tick = self.get_alt_tick(origin_symbol, target_symbol)
        return math.floor(origin_balance * 10 ** origin_tick) / float(
            10 ** origin_tick)

    def _sell_alt(self, origin_coin: Coin,
                  target_coin: Coin):  # pylint: disable=too-many-locals
        """
        Sell altcoin
        """
        trade_log = self.db.start_trade_log(origin_coin, target_coin, True)
        origin_symbol = origin_coin.symbol
        target_symbol = target_coin.symbol

        with self.cache.open_balances() as balances:
            balances.clear()

        origin_balance = self.get_currency_balance(origin_symbol)
        target_balance = self.get_currency_balance(target_symbol)

        pair_info = self.binance_client.get_symbol_info(
            origin_symbol + target_symbol)
        from_coin_price = self.get_ticker_price(origin_symbol + target_symbol)
        from_coin_price_s = "{:0.0{}f}".format(from_coin_price,
                                               pair_info["quotePrecision"])

        order_quantity = self._sell_quantity(origin_symbol, target_symbol,
                                             origin_balance)
        if not order_quantity:
            _logger.info(
                f'skipping selling {origin_symbol}: '
                f'order_quantity invalid {order_quantity}'
            )
            return None
        order_quantity_s = "{:0.0{}f}".format(order_quantity,
                                              pair_info["baseAssetPrecision"])
        _logger.info(f"Selling {order_quantity} of {origin_symbol}")

        _logger.info(f"Balance is {origin_balance}")
        order, transaction_fee = None, 0
        order_guard = self.stream_manager.acquire_order_guard()
        while order is None:
            # Should sell at calculated price to avoid lost coin
            order = self.binance_client.order_limit_sell(
                symbol=origin_symbol + target_symbol, quantity=order_quantity_s,
                price=from_coin_price_s
            )
            transaction_fee = self.get_fee(origin_coin, target_coin,
                                           selling=True)
            _logger.info(order)
            _logger.info("transaction free %s", transaction_fee)

        _logger.info("order success")
        _logger.info(order)

        trade_log.set_ordered(origin_balance, target_balance, order_quantity,
                              transaction_fee)

        order_guard.set_order(origin_symbol, target_symbol,
                              int(order["orderId"]))
        order = self.wait_for_order(order["orderId"], origin_symbol,
                                    target_symbol, order_guard)

        if order is None:
            return None

        new_balance = self.get_currency_balance(origin_symbol)
        while new_balance >= origin_balance:
            new_balance = self.get_currency_balance(origin_symbol, True)

        _logger.info(f"Sold {origin_symbol}")

        trade_log.set_complete(order.cumulative_quote_qty)

        return order
