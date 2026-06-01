from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()


def get_client():

    api_key = os.getenv(
        "BINANCE_API_KEY"
    )

    secret_key = os.getenv(
        "BINANCE_SECRET_KEY"
    )

    client = Client(
        api_key,
        secret_key,
        testnet=True
    )

    return client