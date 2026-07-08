import pandas as pd
from strategies.base_strategy import BaseStrategy
from indicators.indicator_factory import IndicatorFactory
from indicators.indicator_pipeline import IndicatorPipeline


class RSIStrategy(BaseStrategy):

    def __init__(
        self,
        period: int = 14,
        oversold: int = 30,
        overbought: int = 70
    ):

        self.period = period
        self.oversold = oversold
        self.overbought = overbought

    @property
    def name(self) -> str:

        return "RSI Strategy"

    @property
    def parameters(self):

        return {
            "period": self.period,
            "oversold": self.oversold,
            "overbought": self.overbought
        }

    def generate_signals(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        pipeline = (
            IndicatorPipeline()
            .add(
                IndicatorFactory.create(
                    "RSI",
                    period=self.period
                )
            )
        )

        dataframe = pipeline.calculate(
            dataframe
        )

        dataframe["signal"] = 0

        dataframe.loc[
            dataframe["RSI"] < self.oversold,
            "signal"
        ] = 1

        dataframe.loc[
            dataframe["RSI"] > self.overbought,
            "signal"
        ] = -1

        return dataframe