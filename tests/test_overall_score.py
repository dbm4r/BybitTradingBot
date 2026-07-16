from market.market_regime import MarketRegime
from market.regime_result import RegimeResult

from scanner.market_analysis import MarketAnalysis
from scanner.scoring.market_score import MarketScore
from scanner.scoring.overall_scorer import OverallScorer


print("========== OVERALL SCORE ==========\n")


analysis = MarketAnalysis(
    regime=RegimeResult(
        trend=MarketRegime.TRENDING,
        volatility=MarketRegime.LOW_VOLATILITY,
        liquidity=MarketRegime.HIGH_LIQUIDITY,
    ),
    score=MarketScore(
        trend=90,
        volatility=80,
        liquidity=90,
        confidence=0,
    ),
)

scorer = OverallScorer()

print(
    scorer.score(
        analysis
    )
)