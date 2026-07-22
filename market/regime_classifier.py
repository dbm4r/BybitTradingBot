from models.candle_series import CandleSeries
from market.volatility_detector import VolatilityDetector
from market.liquidity_detector import LiquidityDetector
from market.trend_detector import TrendDetector
from market.regime_result import RegimeResult

class RegimeClassifier:

    def __init__(self):

        self.trend_detector = TrendDetector()
        self.volatility_detector = VolatilityDetector()
        self.liquidity_detector = LiquidityDetector()

    def classify(
        self,
        candles: CandleSeries,
    ) -> RegimeResult:

        trend = self.trend_detector.detect(
            candles
        )

        volatility = self.volatility_detector.detect(
            candles
        )

        liquidity = self.liquidity_detector.detect(
            candles
        )

        return RegimeResult(
            trend=trend,
            volatility=volatility,
            liquidity=liquidity,
        )