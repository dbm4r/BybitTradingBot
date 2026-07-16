from market.market_regime import MarketRegime
from market.regime_result import RegimeResult

from scanner.market_analysis import MarketAnalysis
from scanner.scoring.overall_scorer import OverallScorer


print("========== OVERALL SCORER ==========\n")


analysis = MarketAnalysis(
    regime=RegimeResult(
        trend=MarketRegime.TRENDING,
        volatility=MarketRegime.LOW_VOLATILITY,
        liquidity=MarketRegime.HIGH_LIQUIDITY,
    ),
    trend_score=90,
    volatility_score=70,
    liquidity_score=80,
    confidence=85,
)

scorer = OverallScorer()

score = scorer.score(
    analysis
)

print(score)