import pandas as pd
from indicators.indicator_factory import IndicatorFactory
from indicators.indicator_pipeline import IndicatorPipeline
from indicators.sma import SimpleMovingAverage
from strategies.base_strategy import BaseStrategy


class SMACrossoverStrategy(BaseStrategy):

    def __init__(
        self,
        fast_period: int = 20,
        slow_period: int = 50
    ):

        self.fast_period = fast_period
        self.slow_period = slow_period

    @property
    def name(self) -> str:

        return "SMA Crossover"

    @property
    def parameters(self) -> dict:

        return {
            "fast_period": self.fast_period,
            "slow_period": self.slow_period
        }

    def generate_signals(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        
        pipeline = (
            IndicatorPipeline()
            .add(
                IndicatorFactory.create(
                    "SMA",
                    period=self.fast_period
                )
            )
            .add(
                IndicatorFactory.create(
                    "SMA",
                    period=self.slow_period
                )
            )
        )

        dataframe = pipeline.calculate(dataframe)

        dataframe["signal"] = 0

        dataframe.loc[
            dataframe[f"SMA_{self.fast_period}"] >
            dataframe[f"SMA_{self.slow_period}"],
            "signal"
        ] = 1

        dataframe.loc[
            dataframe[f"SMA_{self.fast_period}"] <
            dataframe[f"SMA_{self.slow_period}"],
            "signal"
        ] = -1

        return dataframe