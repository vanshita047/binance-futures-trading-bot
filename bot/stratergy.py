import pandas as pd


class EMACrossoverStrategy:
   
    def __init__(self, fast_period=9, slow_period=21):
        self.fast_period = fast_period
        self.slow_period = slow_period

    def generate_signals(self, df: pd.DataFrame):
        """
        Parameters:
            df (pd.DataFrame): Must contain a 'close' column

        Returns:
            List of tuples:
                (index, signal_type)
                Example: (42, "BUY")
        """

        if "close" not in df.columns:
            raise ValueError("DataFrame must contain 'close' column")

        # Create a copy to avoid modifying original dataframe
        data = df.copy()

        # Calculate EMAs
        data["ema_fast"] = data["close"].ewm(span=self.fast_period).mean()
        data["ema_slow"] = data["close"].ewm(span=self.slow_period).mean()

        signals = []

        # Start from index 1 because we compare with previous candle
        for i in range(1, len(data)):
            prev = data.iloc[i - 1]
            current = data.iloc[i]

            # BUY crossover
            if prev["ema_fast"] < prev["ema_slow"] and current["ema_fast"] > current["ema_slow"]:
                signals.append((i, "BUY"))

            # SELL crossover
            elif prev["ema_fast"] > prev["ema_slow"] and current["ema_fast"] < current["ema_slow"]:
                signals.append((i, "SELL"))

        return signals
    
    from bot.stratergy import EMACrossoverStrategy

    strategy = EMACrossoverStrategy()
    signals = strategy.generate_signals(df)