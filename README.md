# Binance Futures Trading Bot

A Python-based Binance Futures Testnet trading bot with CLI support.

## Features
- Place BUY / SELL orders
- Market and Limit orders
- Input validation
- Logging support
- Binance API integration
- Environment variable support

## Project Structure

```
bot/
├── client.py
├── orders.py
├── validators.py
├── logging_config.py
cli.py
requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Configure

Create `.env`

```env
BINANCE_API_KEY=your_key
BINANCE_SECRET_KEY=your_secret
```

## Run

Market order:

```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

Limit order:

```bash
python cli.py BTCUSDT SELL LIMIT 0.001 --price 90000
```

## Logs

Stored in:

```
logs/trading.log
```

## Author

Shivansh Sharma
