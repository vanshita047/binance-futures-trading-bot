import logging

logger = logging.getLogger(__name__)

def place_market_order(client, symbol, side, quantity):
    logger.info(f"Placing MARKET order | Symbol: {symbol} | Side: {side} | Quantity: {quantity}")
    
    response = client.new_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logger.info(f"Order successful | Order ID: {response['orderId']}")
    return response


def place_limit_order(client, symbol, side, quantity, price):
    logger.info(f"Placing LIMIT order | Symbol: {symbol} | Side: {side} | Quantity: {quantity} | Price: {price}")
    
    response = client.new_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logger.info(f"Order successful | Order ID: {response['orderId']}")
    return response