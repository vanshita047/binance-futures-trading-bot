import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures


class BinanceFuturesClient:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API credentials not found in .env file")

        self.client = UMFutures(key=api_key, secret=api_secret)

    def get_klines(self, symbol, interval, limit=1000):
        return self.client.klines(
            symbol=symbol,
            interval=interval,
            limit=limit
        )