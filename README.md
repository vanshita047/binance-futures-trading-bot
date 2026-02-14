# Binance Futures Trading Bot

## Overview

This project implements a modular Binance Futures Trading Bot built using Python.

The bot supports:
- CLI-based order execution
- EMA Crossover trading strategy
- Backtesting engine
- Input validation
- Modular architecture
- Secure API key management using environment variables

The architecture is designed with scalability, maintainability, and separation of concerns in mind.

---

## Project Structure

```
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── config.py
│   ├── exchange.py
│   ├── strategy.py
│   ├── backtester.py
│   ├── validators.py
│
├── cli.py
├── requirements.txt
├── README.md
├── sample_execution_log.txt
└── .gitignore
```

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/vanshita047/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment Variables

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```

Important:
- Do NOT commit `.env`
- Ensure `.env` is added to `.gitignore`

---

## Running the Bot

### Place a Futures Order

```bash
python cli.py order --symbol BTCUSDT --side BUY --quantity 0.01
```

### Run Backtest

```bash
python cli.py backtest --symbol BTCUSDT
```

---

## Strategy Explanation

The bot implements an **EMA Crossover Strategy**:

- Buy Signal: Short-term EMA crosses above Long-term EMA
- Sell Signal: Short-term EMA crosses below Long-term EMA

This strategy captures short-term momentum shifts and trend reversals.

---

## Backtesting Engine

The backtester:

- Fetches historical price data
- Applies trading strategy logic
- Calculates profit and loss (PnL)
- Outputs performance metrics

Performance metrics may include:
- Total Return
- Number of Trades
- Win/Loss Ratio
- Cumulative Profit

---

## Security

- API keys are stored using environment variables
- `.env` file is excluded via `.gitignore`
- No secrets are stored in source code
- Repository does not expose sensitive credentials

---

## Sample Execution Logs

Example execution output is included in:

```
sample_execution_log.txt
```

This demonstrates successful CLI execution and backtest runs.

---

## Requirements

Dependencies are listed in `requirements.txt`:

- python-binance
- pandas
- python-dotenv

Install using:

```bash
pip install -r requirements.txt
```

---

## Design Considerations

- Modular folder structure
- Clear separation between exchange, strategy, validation, and CLI
- Extensible architecture for adding new strategies
- Clean and maintainable codebase

---

## Author

Vanshita

---

## Disclaimer

This project is for educational and demonstration purposes only.
Use at your own risk when trading live markets.