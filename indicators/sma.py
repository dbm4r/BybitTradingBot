from indicators.base_indicator import BaseIndicator
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


class SimpleMovingAverage(BaseIndicator):

    def __init__(self, period: int):
        if period <= 0:
            raise ValueError("Period must be greater than zero.")

        self.period = period

    @property
    def name(self) -> str:
        return "SMA"

    @property
    def output_name(self) -> str:
        return f"SMA_{self.period}"

    @property
    def parameters(self) -> dict:
        return {
            "period": self.period
        }

    def calculate(
        self,
        series: CandleSeries,
    ) -> IndicatorResult:

        closes = series.close_prices
        values: list[float | None] = []

        for i in range(len(closes)):

            if i + 1 < self.period:
                values.append(None)
                continue

            window = closes[
                i + 1 - self.period:
                i + 1
            ]

            values.append(
                sum(window) / self.period
            )

        return IndicatorResult(
            name=self.name,
            output_name=self.output_name,
            values=values,
            parameters=self.parameters,
        )