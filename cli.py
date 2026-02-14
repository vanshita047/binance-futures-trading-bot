# from dotenv import load_dotenv
# import os

# load_dotenv()

# print("API KEY:", os.getenv("BINANCE_API_KEY"))

# from bot.logging_config import setup_logger

# logger = setup_logger()

# logger.info("Trading bot started")
# print("Logger test complete")

import time
from bot.client import BinanceFuturesClient
import logging

SYMBOL = "BTCUSDT"
INTERVAL = "1m"

def main():

    logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )
    client = BinanceFuturesClient()
    logging.info("Bot started...")

    while True:
        try:
            klines = client.get_klines(
                symbol=SYMBOL,
                interval=INTERVAL,
                limit=10
            )

            latest_candle = klines[-1]
            close_price = latest_candle[4]

            print(f"Latest Close Price: {close_price}")

            time.sleep(60)

        except Exception as e:
            print("Error:", e)
            time.sleep(10)


if __name__ == "__main__":
    main()