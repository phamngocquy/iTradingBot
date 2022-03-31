# coding=utf-8
import logging

__author__ = 'qPham'

from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from src.config import Config
from src.database import Database
from src.binance_api_manager import BinanceAPIManager
from src.models import Coin, CoinValue

_logger = logging.getLogger(__name__)


class Strategy:
    """
        Define specify strategy
    """

    def __init__(self, binance_manager: BinanceAPIManager,
                 database: Database,
                 config: Config):
        self.manager = binance_manager
        self.db = database
        self.config = config

    def initialize(self):
        """
        Initial necessary data
        :return:
        """
        alt_coins = self.manager.get_all_symbol()
        self.db.set_coins(symbols=alt_coins)
        _logger.info('strategy initialize: Done')

    def scout(self):
        """
        Get top gainers 24h
        :return:
        """
        _logger.info('>>>>>>>>>>> Scouting')
        alt_coin_gainer24hr = self.manager.get_top_alt_gainer24hr(
            topn=self.config.TOP_24HR_GAINER
        )
        _logger.info(alt_coin_gainer24hr)

        _logger.info('>>>>>>>>>>> Sell all current alt coin to bridge')
        self.sell_all_alt_coin()

        _logger.info('>>>>>>>>>>> Buy alt coin in top 24hr gainer on bridge')
        self.buy_alt_coins(alt_coin_gainer24hr)

        _logger.info('>>>>>>>>>>> FINISH jumping')

    def sell_all_alt_coin(self):
        """
        sell all alt_coin in wallet
        :return:
        """
        alt_coin_balance = self.manager.get_balance()
        for item in alt_coin_balance.keys():
            alt_coin = self.db.get_coin(item)
            if not alt_coin:
                continue
            self.sell_alt_coin(alt_coin)
            self.db.update_coin(alt_coin, {'enabled': False})

    def buy_alt_coins(self, symbols: List[str]):
        """
        :param symbols:
        :return:
        """

        n_alt_coin = len(symbols)
        for symbol in symbols:
            bridge_balance = self.manager.get_currency_balance(
                self.config.BRIDGE.symbol, force=True
            )
            alt_coin = self.db.get_coin(symbol)
            buy_balance = bridge_balance // n_alt_coin
            n_alt_coin -= 1
            if not alt_coin:
                _logger.info(f'Coin symbol Invalid: {Coin.symbol}')
                continue
            _logger.info(
                f'Buy in {alt_coin.symbol} '
                f'with {buy_balance} {self.config.BRIDGE.symbol}'
            )
            self.manager.buy_alt(alt_coin, self.config.BRIDGE, buy_balance)
            self.db.update_coin(alt_coin, {'enabled': True})

    def update_values(self):
        """
        Log current value state of all
        altcoin balances against BTC and USDT in DB.
        """

        now = datetime.now()

        session: Session
        with self.db.db_session() as session:
            coins: List[Coin] = session.query(Coin).all()
            for coin in coins:
                balance = self.manager.get_currency_balance(coin.symbol)
                if balance == 0:
                    continue
                usd_value = self.manager.get_ticker_price(coin + "USDT")
                btc_value = self.manager.get_ticker_price(coin + "BTC")
                coin_value = CoinValue(
                    coin, balance, usd_value,
                    btc_value, datetime=now
                )
                session.add(coin_value)
                self.db.send_update(coin_value)

    def sell_alt_coin(self, alt_coin: Coin):
        """
        Jump from the source coin to the destination coin through bridge coin
        """
        can_sell = False
        balance = self.manager.get_currency_balance(alt_coin.symbol)
        from_coin_price = self.manager.get_ticker_price(
            alt_coin.symbol + self.config.BRIDGE.symbol
        )

        if balance and alt_coin.symbol != self.config.BRIDGE.symbol and \
                balance * from_coin_price > self.manager.get_min_notional(
            alt_coin.symbol, self.config.BRIDGE.symbol
        ):
            can_sell = True
        else:
            _logger.info("Skipping sell")

        result = self.manager.sell_alt(alt_coin, self.config.BRIDGE)
        if can_sell and not result:
            _logger.info("Couldn't sell, going back to scouting mode...")
            return None
        return result
