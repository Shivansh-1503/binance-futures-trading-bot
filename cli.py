import argparse
from bot.orders import place_order


def trade():

    parser = argparse.ArgumentParser()

    parser.add_argument("symbol")
    parser.add_argument("side")
    parser.add_argument("order_type")
    parser.add_argument("quantity", type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        result = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nORDER SUCCESS")
        print(result)

    except Exception as e:
        print("\nFAILED")
        print(str(e))


if __name__ == "__main__":
    trade()