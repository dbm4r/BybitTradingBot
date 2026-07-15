from models.candle_series import CandleSeries
from indicators.atr import AverageTrueRange
from market.market_regime import MarketRegime
from market.regime_detector import RegimeDetector

class VolatilityDetector(RegimeDetector):

    def __init__(
        self,
        period: int = 14,
        threshold: float = 0.01,
    ):

        self.atr = AverageTrueRange(
            period
        )

        self.threshold = threshold
    def detect(
        self,
        candles: CandleSeries,
    ) -> MarketRegime:

        result = self.atr.calculate(
            candles
        )

        atr = result.last

        price = candles.last.close

        if (
            atr is None
            or price == 0
        ):
            return MarketRegime.UNKNOWN

        volatility = atr / price

        if volatility >= self.threshold:
            return MarketRegime.HIGH_VOLATILITY

        return MarketRegime.LOW_VOLATILITY