from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    try:

        payload = {
            "symbol": symbol,
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type.upper() == "LIMIT":

            payload["price"] = price
            payload["timeInForce"] = "GTC"

        logger.info(f"REQUEST -> {payload}")

        result = client.futures_create_order(
            **payload
        )

        logger.info(f"RESPONSE -> {result}")

        return result

    except Exception as e:

        logger.error(str(e))
        raise