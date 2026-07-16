from market.market_regime import MarketRegime
from market.regime_result import RegimeResult

from scanner.scoring.base_scorer import BaseScorer


class LiquidityScorer(BaseScorer):

    def score(
        self,
        regime: RegimeResult,
    ) -> float:

        if regime is None:
            return 0.0

        if regime.liquidity == MarketRegime.HIGH_LIQUIDITY:
            return 90.0

        if regime.liquidity == MarketRegime.LOW_LIQUIDITY:
            return 40.0

        return 0.0