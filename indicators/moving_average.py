import pandas as pd

from indicators.base_indicator import BaseIndicator


class SimpleMovingAverage(BaseIndicator):

    def __init__(self, period: int):

        self.period = period

    @property
    def name(self) -> str:

        return "Simple Moving Average"

    @property
    def parameters(self) -> dict:

        return {
            "period": self.period
        }

    def calculate(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        column_name = f"SMA_{self.period}"

        dataframe[column_name] = (
            dataframe["close"]
            .rolling(window=self.period)
            .mean()
        )

        return dataframe