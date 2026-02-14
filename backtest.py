import pandas as pd
import matplotlib.pyplot as plt
from bot.client import BinanceFuturesClient
from bot.strategy import EMACrossoverStrategy


INITIAL_BALANCE = 10000
RISK_PER_TRADE = 0.01
STOP_LOSS_PERCENT = 0.02
TAKE_PROFIT_PERCENT = 0.03


def load_data():
    client = BinanceFuturesClient()

    klines = client.get_klines(
        symbol="BTCUSDT",
        interval="1m",
        limit=1000
    )

    df = pd.DataFrame(klines)

    df.columns = [
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "qav", "trades", "tbbav", "tbqav", "ignore"
    ]

    df["close"] = df["close"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)

    return df


def calculate_max_drawdown(equity_curve):
    peak = equity_curve[0]
    max_dd = 0

    for value in equity_curve:
        if value > peak:
            peak = value

        drawdown = (peak - value) / peak
        if drawdown > max_dd:
            max_dd = drawdown

    return max_dd * 100


def plot_equity_curve(equity_curve):
    plt.figure(figsize=(10, 5))
    plt.plot(equity_curve)
    plt.title("Equity Curve")
    plt.xlabel("Trades")
    plt.ylabel("Balance")
    plt.grid(True)
    plt.show()


def run_backtest():
    df = load_data()
    strategy = EMACrossoverStrategy()

    signals = strategy.generate_signals(df)

    balance = INITIAL_BALANCE
    equity_curve = [balance]

    wins = 0
    losses = 0
    gross_profit = 0
    gross_loss = 0

    for index, signal in signals:

        entry_price = df.iloc[index]["close"]
        risk_amount = balance * RISK_PER_TRADE

        if signal == "BUY":
            sl = entry_price * (1 - STOP_LOSS_PERCENT)
            tp = entry_price * (1 + TAKE_PROFIT_PERCENT)
        else:
            sl = entry_price * (1 + STOP_LOSS_PERCENT)
            tp = entry_price * (1 - TAKE_PROFIT_PERCENT)

        for j in range(index + 1, len(df)):
            high = df.iloc[j]["high"]
            low = df.iloc[j]["low"]

            if signal == "BUY":
                if low <= sl:
                    balance -= risk_amount
                    gross_loss += risk_amount
                    losses += 1
                    break

                if high >= tp:
                    reward = risk_amount * (TAKE_PROFIT_PERCENT / STOP_LOSS_PERCENT)
                    balance += reward
                    gross_profit += reward
                    wins += 1
                    break

            else:
                if high >= sl:
                    balance -= risk_amount
                    gross_loss += risk_amount
                    losses += 1
                    break

                if low <= tp:
                    reward = risk_amount * (TAKE_PROFIT_PERCENT / STOP_LOSS_PERCENT)
                    balance += reward
                    gross_profit += reward
                    wins += 1
                    break

        equity_curve.append(balance)

    total_trades = wins + losses
    win_rate = (wins / total_trades * 100) if total_trades > 0 else 0
    total_return = ((balance - INITIAL_BALANCE) / INITIAL_BALANCE) * 100
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else 0
    max_drawdown = calculate_max_drawdown(equity_curve)

    print("\n====== BACKTEST RESULTS ======")
    print(f"Initial Balance: ${INITIAL_BALANCE}")
    print(f"Final Balance: ${round(balance, 2)}")
    print(f"Total Return: {round(total_return, 2)}%")
    print(f"Total Trades: {total_trades}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win Rate: {round(win_rate, 2)}%")
    print(f"Profit Factor: {round(profit_factor, 2)}")
    print(f"Max Drawdown: {round(max_drawdown, 2)}%")
    print("==============================\n")

    plot_equity_curve(equity_curve)


if __name__ == "__main__":
    run_backtest()