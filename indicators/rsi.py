import pandas as pd

from indicators.base_indicator import BaseIndicator


class RelativeStrengthIndex(BaseIndicator):

    def __init__(
        self,
        period: int = 14
    ):

        self.period = period

    @property
    def name(self) -> str:

        return "Relative Strength Index"

    @property
    def parameters(self) -> dict:

        return {
            "period": self.period
        }

    def calculate(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        delta = dataframe["close"].diff()

        gain = delta.where(
            delta > 0,
            0
        )

        loss = -delta.where(
            delta < 0,
            0
        )

        average_gain = gain.rolling(
            self.period
        ).mean()

        average_loss = loss.rolling(
            self.period
        ).mean()

        rs = average_gain / average_loss

        dataframe["RSI"] = (
            100 -
            (100 / (1 + rs))
        )

        return dataframe