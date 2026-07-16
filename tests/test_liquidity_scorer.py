from market.market_regime import MarketRegime
from market.regime_result import RegimeResult

from scanner.scoring.liquidity_scorer import LiquidityScorer


print("========== LIQUIDITY SCORER ==========\n")


regime = RegimeResult(
    trend=MarketRegime.TRENDING,
    volatility=MarketRegime.LOW_VOLATILITY,
    liquidity=MarketRegime.HIGH_LIQUIDITY,
)

scorer = LiquidityScorer()

print(
    scorer.score(
        regime
    )
)