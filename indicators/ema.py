import pandas as pd

from indicators.base_indicator import BaseIndicator


class ExponentialMovingAverage(BaseIndicator):

    def __init__(
        self,
        period: int
    ):

        self.period = period

    @property
    def name(self) -> str:

        return "Exponential Moving Average"

    @property
    def parameters(self) -> dict:

        return {
            "period": self.period
        }

    def calculate(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        column = f"EMA_{self.period}"

        dataframe[column] = (
            dataframe["close"]
            .ewm(
                span=self.period,
                adjust=False
            )
            .mean()
        )

        return dataframe