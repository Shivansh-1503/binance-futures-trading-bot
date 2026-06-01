import typer

from bot.orders import place_order
from bot.validators import validate_order

app = typer.Typer()


@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):

    try:

        validate_order(order_type, price)

        result = place_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\nSUCCESS")
        print(result)

    except Exception as e:

        print("\nFAILED")
        print(str(e))


if __name__ == "__main__":
    app()