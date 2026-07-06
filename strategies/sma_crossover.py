import pandas as pd

from indicators.moving_average import SimpleMovingAverage
from strategies.base_strategy import BaseStrategy


class SMACrossoverStrategy(BaseStrategy):

    def __init__(self, fast_period: int = 20, slow_period: int = 50):

        self.fast_period = fast_period
        self.slow_period = slow_period

    def generate_signals(self, df: pd.DataFrame):

        fast_sma = SimpleMovingAverage(self.fast_period)
        slow_sma = SimpleMovingAverage(self.slow_period)

        df = fast_sma.calculate(df)
        df = slow_sma.calculate(df)

        df["signal"] = 0

        df.loc[
            df[f"SMA_{self.fast_period}"] >
            df[f"SMA_{self.slow_period}"],
            "signal"
        ] = 1

        df.loc[
            df[f"SMA_{self.fast_period}"] <
            df[f"SMA_{self.slow_period}"],
            "signal"
        ] = -1

        return df