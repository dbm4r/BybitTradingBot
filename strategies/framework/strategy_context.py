from dataclasses import dataclass
from indicators.base_indicator import BaseIndicator
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


@dataclass(frozen=True)
class StrategyContext:

    candles: CandleSeries

    indicators: dict[str, IndicatorResult]

    def get_indicator(
        self,
        indicator: BaseIndicator,
    ) -> IndicatorResult | None:

        return self.indicators.get(
            indicator.output_name
        )