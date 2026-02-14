import logging

logger = logging.getLogger(__name__)

def validate_order_input(args):
    """
    Validates CLI input arguments before placing order.
    """

    # Validate symbol
    if not args.symbol or not isinstance(args.symbol, str):
        raise ValueError("Invalid symbol provided.")

    # Validate quantity
    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    # Validate order type specific rules
    if args.type == "LIMIT":
        if args.price is None:
            raise ValueError("LIMIT order requires --price.")
        if args.price <= 0:
            raise ValueError("Price must be greater than 0.")

    logger.info("Input validation successful.")