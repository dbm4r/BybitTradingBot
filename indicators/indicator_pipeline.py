from indicators.base_indicator import BaseIndicator
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult
from collections.abc import Iterator

class IndicatorPipeline:

    def __init__(self):
        self._indicators: dict[str, BaseIndicator] = {}

    def add(
        self,
        indicator: BaseIndicator,
    ) -> "IndicatorPipeline":

        if not isinstance(indicator, BaseIndicator):
            raise TypeError(
                "Expected a BaseIndicator instance."
            )

        self._indicators[indicator.output_name] = indicator

        return self

    def add_many(
        self,
        *indicators: BaseIndicator,
    ) -> "IndicatorPipeline":

        for indicator in indicators:
            self.add(indicator)

        return self

    def get(
        self,
        output_name: str,
    ) -> BaseIndicator | None:

        return self._indicators.get(output_name)

    def has(
        self,
        output_name: str,
    ) -> bool:

        return output_name in self._indicators

    def remove(
        self,
        output_name: str,
    ) -> None:

        self._indicators.pop(output_name, None)

    def calculate(
        self,
        series: CandleSeries,
    ) -> dict[str, IndicatorResult]:

        results: dict[str, IndicatorResult] = {}

        for indicator in self._indicators.values():

            result = indicator.calculate(series)

            results[result.output_name] = result

        return results

    @property
    def indicators(self) -> tuple[BaseIndicator, ...]:
        return tuple(self._indicators.values())

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

    def __iter__(self) -> Iterator[BaseIndicator]:
        return iter(self._indicators.values())