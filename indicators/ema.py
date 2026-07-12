from indicators.period_indicator import PeriodIndicator
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult



class ExponentialMovingAverage(PeriodIndicator):


    @property
    def name(self) -> str:
        return "EMA"

    @property
    def output_name(self) -> str:
        return f"EMA_{self.period}"

    def calculate(
        self,
        series: CandleSeries,
    ) -> IndicatorResult:

        closes = series.close_prices

        values: list[float | None] = []

        multiplier = 2 / (self.period + 1)

        ema: float | None = None

        for i, close in enumerate(closes):

            if i + 1 < self.period:
                values.append(None)
                continue

            if ema is None:
                ema = sum(
                    closes[
                        i + 1 - self.period:
                        i + 1
                    ]
                ) / self.period

            else:
                ema = (
                    (close - ema)
                    * multiplier
                    + ema
                )

            values.append(ema)

        return IndicatorResult(
            name=self.name,
            output_name=self.output_name,
            values=values,
            parameters=self.parameters,
        )