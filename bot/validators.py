def validate_order(order_type, price):

    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError(
            "Order type must be MARKET or LIMIT"
        )

    if order_type == "LIMIT" and price is None:
        raise ValueError(
            "Price is required for LIMIT orders"
        )