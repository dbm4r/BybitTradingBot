from models.candle_series import CandleSeries

from indicators.ema import ExponentialMovingAverage

from market.market_regime import MarketRegime
from market.regime_detector import RegimeDetector


class TrendDetector(RegimeDetector):

    def __init__(
        self,
        fast_period: int = 20,
        slow_period: int = 50,
    ):

        self.fast_indicator = ExponentialMovingAverage(
            fast_period
        )

        self.slow_indicator = ExponentialMovingAverage(
            slow_period
        )

    def detect(
        self,
        candles: CandleSeries,
    ) -> MarketRegime:

        fast = self.fast_indicator.calculate(
            candles
        )

        slow = self.slow_indicator.calculate(
            candles
        )

        fast_value = fast.last
        slow_value = slow.last

        if (
            fast_value is None
            or slow_value is None
        ):
            return MarketRegime.UNKNOWN

        if fast_value > slow_value:
            return MarketRegime.TRENDING

        return MarketRegime.RANGING