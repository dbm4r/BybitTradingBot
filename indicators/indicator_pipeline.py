from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult

from indicators.base_indicator import BaseIndicator


class IndicatorPipeline:

    def __init__(self):
        self._indicators: list[BaseIndicator] = []

    def add(
        self,
        indicator: BaseIndicator,
    ) -> "IndicatorPipeline":
        self._indicators.append(indicator)
        return self

    def calculate(
        self,
        series: CandleSeries,
    ) -> dict[str, IndicatorResult]:

        results: dict[str, IndicatorResult] = {}

        for indicator in self._indicators:

            result = indicator.calculate(series)

            results[result.output_name] = result

        return results

    @property
    def indicators(self) -> tuple[BaseIndicator, ...]:
        return tuple(self._indicators)

    @property
    def count(self) -> int:
        return len(self._indicators)

    @property
    def is_empty(self) -> bool:
        return len(self._indicators) == 0

    def clear(self) -> None:
        self._indicators.clear()

    def __len__(self) -> int:
        return len(self._indicators)

    def __iter__(self):
        return iter(self._indicators)