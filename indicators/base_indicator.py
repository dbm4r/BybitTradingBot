from abc import ABC, abstractmethod

from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult


class BaseIndicator(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Short identifier.

        Example:
            EMA
            SMA
            RSI
        """
        pass

    @property
    @abstractmethod
    def output_name(self) -> str:
        """
        Output name.

        Example:
            EMA_20
            SMA_50
            RSI_14
        """
        pass

    @property
    @abstractmethod
    def parameters(self) -> dict:
        pass

    @abstractmethod
    def calculate(
        self,
        series: CandleSeries,
    ) -> IndicatorResult:
        pass