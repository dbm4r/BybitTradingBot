from indicators.period_indicator import PeriodIndicator
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


class AverageTrueRange(PeriodIndicator):

    @property
    def name(self) -> str:
        return "ATR"

    @property
    def output_name(self) -> str:
        return f"ATR_{self.period}"

    def calculate(
        self,
        series: CandleSeries,
    ) -> IndicatorResult:

        highs = series.high_prices
        lows = series.low_prices
        closes = series.close_prices

        values: list[float | None] = []
        true_ranges: list[float] = []

        for i in range(len(closes)):

            if i == 0:

                true_ranges.append(
                    highs[i] - lows[i]
                )

                continue

            previous_close = closes[i - 1]

            range1 = highs[i] - lows[i]

            range2 = abs(
                highs[i] - previous_close
            )

            range3 = abs(
                lows[i] - previous_close
            )

            true_ranges.append(
                max(
                    range1,
                    range2,
                    range3,
                )
            )

        for i in range(len(true_ranges)):

            if i + 1 < self.period:

                values.append(None)

                continue

            window = true_ranges[
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