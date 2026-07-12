from indicators.base_indicator import BaseIndicator
from indicators.indicator_factory import IndicatorFactory
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


class DummyIndicator(BaseIndicator):

    @property
    def name(self):
        return "Dummy"

    @property
    def output_name(self):
        return "Dummy"

    @property
    def parameters(self):
        return {}

    def calculate(
        self,
        series: CandleSeries,
    ) -> IndicatorResult:

        return IndicatorResult(
            name=self.name,
            output_name=self.output_name,
            values=[],
            parameters={},
        )


IndicatorFactory.register(
    "DUMMY",
    DummyIndicator,
)

indicator = IndicatorFactory.create("DUMMY")

print(type(indicator).__name__)
try:
    IndicatorFactory.register(
        "DUMMY",
        DummyIndicator,
    )
except ValueError as e:
    print(e)