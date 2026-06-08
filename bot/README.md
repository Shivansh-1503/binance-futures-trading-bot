# Binance Futures Testnet Trading Bot

Python CLI application for placing market and limit orders.

## Run

python cli.py trade



# Binance Futures Testnet Trading Bot

A simple Python CLI application for placing Market and Limit orders on Binance Futures Testnet (USDT-M).

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* CLI input handling
* Validation and exception handling
* Logging of requests and responses

## Setup

Create virtual environment:

python -m venv venv

Activate:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create .env:

BINANCE_API_KEY=your_api_key

BINANCE_SECRET_KEY=your_secret_key

## Run Examples

Market Order:

python cli.py BTCUSDT BUY MARKET 0.001

Limit Order:

python cli.py BTCUSDT SELL LIMIT 0.001 --price 90000

Example:

python cli.py BTCUSDT BUY MARKET 0.001
python cli.py BTCUSDT BUY LIMIT 0.001 --price 65000
## Logs

Logs are stored inside:

logs/trading.log

## Assumptions

* Binance Futures Testnet used
* USDT-M supported
* Valid API credentials required
