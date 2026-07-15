from models.candle_series import CandleSeries

from market.market_regime import MarketRegime
from market.regime_detector import RegimeDetector


class LiquidityDetector(RegimeDetector):

    def __init__(
        self,
        period: int = 20,
        threshold: float = 1.0,
    ):

        self.period = period
        self.threshold = threshold

    def detect(
        self,
        candles: CandleSeries,
    ) -> MarketRegime:

        volumes = candles.volumes

        if len(volumes) < self.period:
            return MarketRegime.UNKNOWN

        window = volumes[-self.period:]

        average_volume = sum(window) / self.period

        current_volume = candles.last_volume

        if (
            current_volume is None
            or average_volume == 0
        ):
            return MarketRegime.UNKNOWN

        liquidity = current_volume / average_volume

        if liquidity >= self.threshold:
            return MarketRegime.HIGH_LIQUIDITY

        return MarketRegime.LOW_LIQUIDITY