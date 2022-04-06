#!python3
import logging
import time

from src.binance_api_manager import BinanceAPIManager
from src.config import Config
from src.database import Database
from src.scheduler import SafeScheduler
from src.strategy import get_strategy

_logger = logging.getLogger(__name__)


def main():
    _logger.info("Starting")

    config = Config()
    db = Database(config)
    manager = BinanceAPIManager(config, db)
    try:
        _ = manager.get_account()
    except Exception as e:
        _logger.error("Couldn't access Binance API - "
                      "API keys may be wrong or lack sufficient permissions")
        _logger.error(e)
        return

    strategy = get_strategy(config.STRATEGY)
    if strategy is None:
        _logger.error("Invalid strategy name")
        return
    trader = strategy(manager, db, config)
    _logger.info(f"Chosen strategy: {config.STRATEGY}")

    _logger.info("Creating database schema if it doesn't already exist")
    db.create_database()

    db.migrate_old_state()

    trader.initialize()

    schedule = SafeScheduler()
    schedule.every(config.SCOUT_SLEEP_TIME) \
        .hours.do(trader.scout).tag("scouting")
    # schedule.run_all()

    schedule.every(10).seconds.do(trader.update_values) \
        .tag("updating value history")
    schedule.every(1).minutes.do(db.prune_scout_history).tag(
        "pruning scout history")
    schedule.every(1).hours.do(db.prune_value_history).tag(
        "pruning value history")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    finally:
        manager.stream_manager.close()
