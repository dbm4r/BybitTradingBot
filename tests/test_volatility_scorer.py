from market.market_regime import MarketRegime
from market.regime_result import RegimeResult

from scanner.scoring.volatility_scorer import VolatilityScorer


print("========== VOLATILITY SCORER ==========\n")


regime = RegimeResult(
    trend=MarketRegime.TRENDING,
    volatility=MarketRegime.LOW_VOLATILITY,
    liquidity=MarketRegime.HIGH_LIQUIDITY,
)

scorer = VolatilityScorer()

print(
    scorer.score(
        regime
    )
)