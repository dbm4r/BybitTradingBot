from functools import cached_property

from indicators.base_indicator import BaseIndicator
from indicators.validation import IndicatorValidator


class PeriodIndicator(BaseIndicator):

    def __init__(self, period: int):
        IndicatorValidator.validate_period(period)

        self._period = period

    @cached_property
    def parameters(self) -> dict:
        return {
            "period": self.period
        }
    @property
    def period(self) -> int:
        return self._period