from dataclasses import dataclass

from indicators.base_indicator import BaseIndicator
from models.candle import Candle
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


@dataclass(slots=True, frozen=True)
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

    @property
    def last_candle(self) -> Candle:

        return self.candles.last