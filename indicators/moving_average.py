import pandas as pd
from indicators.base_indicator import BaseIndicator


class SimpleMovingAverage(BaseIndicator):

    def __init__(self, period: int):
        self.period = period

    def calculate(self, df: pd.DataFrame):

        column_name = f"SMA_{self.period}"

        df[column_name] = (
            df["close"]
            .rolling(window=self.period)
            .mean()
        )

        return df