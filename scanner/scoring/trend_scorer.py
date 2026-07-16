from market.market_regime import MarketRegime
from market.regime_result import RegimeResult

from scanner.scoring.base_scorer import BaseScorer


class TrendScorer(BaseScorer):

    def score(
        self,
        regime: RegimeResult,
    ) -> float:

        if regime is None:
            return 0.0

        if regime.trend == MarketRegime.TRENDING:
            return 90.0

        if regime.trend == MarketRegime.RANGING:
            return 40.0

        return 0.0