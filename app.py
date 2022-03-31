import logging.config
from src.crypto_trading import main as run_trader

logging.config.fileConfig(
    fname='config/logging.ini', disable_existing_loggers=False
)

if __name__ == '__main__':
    run_trader()
