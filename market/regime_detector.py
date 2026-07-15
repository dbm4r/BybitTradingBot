from abc import ABC, abstractmethod

from models.candle_series import CandleSeries
from market.market_regime import MarketRegime


class RegimeDetector(ABC):

    @abstractmethod
    def detect(
        self,
        candles: CandleSeries,
    ) -> MarketRegime:
        pass