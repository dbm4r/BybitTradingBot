from dataclasses import dataclass

from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


@dataclass(frozen=True)
class StrategyContext:

    candles: CandleSeries

    indicators: dict[str, IndicatorResult]

    def get_indicator(
        self,
        output_name: str,
    ) -> IndicatorResult | None:

        return self.indicators.get(output_name)