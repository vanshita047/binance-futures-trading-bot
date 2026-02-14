import argparse
import logging
import sys

from bot.logging_config import setup_logging
from bot.client import BinanceFuturesClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order_input

# Setup logging FIRST
setup_logging()
logger = logging.getLogger(__name__)
logger.info("Bot started...")


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Validate input
        validate_order_input(args)

        # Initialize client
        client = BinanceFuturesClient().client

        if args.type == "MARKET":
            place_market_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )

        elif args.type == "LIMIT":
            if not args.price:
                raise ValueError("LIMIT order requires --price")

            place_limit_order(
                client=client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()