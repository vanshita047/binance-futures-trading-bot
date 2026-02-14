import pandas as pd


class EMACrossoverStrategy:

    def __init__(self, short_window=9, long_window=21):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, df):

        df["ema_short"] = df["close"].ewm(span=self.short_window, adjust=False).mean()
        df["ema_long"] = df["close"].ewm(span=self.long_window, adjust=False).mean()

        signals = []

        for i in range(1, len(df)):

            # BUY signal
            if (
                df["ema_short"].iloc[i] > df["ema_long"].iloc[i]
                and df["ema_short"].iloc[i - 1] <= df["ema_long"].iloc[i - 1]
            ):
                signals.append((i, "BUY"))

            # SELL signal
            elif (
                df["ema_short"].iloc[i] < df["ema_long"].iloc[i]
                and df["ema_short"].iloc[i - 1] >= df["ema_long"].iloc[i - 1]
            ):
                signals.append((i, "SELL"))

        return signals