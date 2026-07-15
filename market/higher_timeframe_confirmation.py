from market.timeframe import Timeframe
from market.trend_detector import TrendDetector
from market.market_regime import MarketRegime


class HigherTimeframeConfirmation:

    @staticmethod
    def confirms(
        context,
        strategy,
    ) -> bool:

        if not strategy.requires_higher_timeframe_confirmation:
            return True

        if context.timeframes is None:
            return False

        detector = TrendDetector()

        for timeframe in strategy.confirmation_timeframes:

            series = context.timeframes.get(
                timeframe.value
            ).candles

            trend = detector.detect(
                series
            )

            if trend != MarketRegime.TRENDING:
                return False

        return True