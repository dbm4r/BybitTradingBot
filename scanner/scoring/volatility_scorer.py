from market.market_regime import MarketRegime
from market.regime_result import RegimeResult

from scanner.scoring.base_scorer import BaseScorer


class VolatilityScorer(BaseScorer):

    def score(
        self,
        regime: RegimeResult,
    ) -> float:

        if regime is None:
            return 0.0

        if regime.volatility == MarketRegime.LOW_VOLATILITY:
            return 80.0

        if regime.volatility == MarketRegime.HIGH_VOLATILITY:
            return 60.0

        return 0.0