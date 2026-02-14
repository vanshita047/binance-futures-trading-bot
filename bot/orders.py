from bot.client import BinanceFuturesClient


class OrderManager:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_market_order(self, symbol, side, quantity):
        return self.client.place_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    def place_limit_order(self, symbol, side, quantity, price):
        return self.client.place_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )