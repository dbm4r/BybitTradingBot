from dataclasses import dataclass, field

from indicators.indicator_pipeline import IndicatorPipeline
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


@dataclass(slots=True)
class TimeframeContext:

    timeframe: str

    candles: CandleSeries

    indicator_pipeline: IndicatorPipeline = field(
        default_factory=IndicatorPipeline
    )

    indicators: dict[str, IndicatorResult] = field(
        default_factory=dict
    )

    def calculate_indicators(self) -> None:

        self.indicators = (
            self.indicator_pipeline.calculate(
                self.candles
            )
        )
    def add_indicators(
        self,
        *indicators,
    ) -> None:

        self.indicator_pipeline.add_many(
            *indicators
        )