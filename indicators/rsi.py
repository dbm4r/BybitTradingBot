from functools import cached_property

from indicators.base_indicator import BaseIndicator
from indicators.validation import IndicatorValidator
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


class RSI(BaseIndicator):

    def __init__(
        self,
        period: int = 14,
    ):
        IndicatorValidator.validate_period(period)

        self.period = period

    @property
    def name(self) -> str:
        return "RSI"

    @property
    def output_name(self) -> str:
        return f"RSI_{self.period}"

    @cached_property
    def parameters(self) -> dict:
        return {
            "period": self.period
        }

    def calculate(
        self,
        series: CandleSeries,
    ) -> IndicatorResult:

        closes = series.close_prices

        values: list[float | None] = [None] * len(closes)

        if len(closes) <= self.period:
            return IndicatorResult(
                name=self.name,
                output_name=self.output_name,
                values=values,
                parameters=self.parameters,
            )

        gains: list[float] = []
        losses: list[float] = []

        for i in range(1, len(closes)):
            delta = closes[i] - closes[i - 1]

            gains.append(max(delta, 0))
            losses.append(max(-delta, 0))

        for i in range(self.period, len(closes)):

            average_gain = (
                sum(gains[i - self.period:i])
                / self.period
            )

            average_loss = (
                sum(losses[i - self.period:i])
                / self.period
            )

            if average_loss == 0:
                values[i] = 100.0
                continue

            rs = average_gain / average_loss

            values[i] = 100 - (100 / (1 + rs))

        return IndicatorResult(
            name=self.name,
            output_name=self.output_name,
            values=values,
            parameters=self.parameters,
        )