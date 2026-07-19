from market.market_regime import MarketRegime
from market.regime_result import RegimeResult
from scanner.scoring.market_score import MarketScore
from scanner.market_analysis import MarketAnalysis
from scanner.scoring.overall_scorer import OverallScorer


print("========== OVERALL SCORER ==========\n")


analysis = MarketAnalysis(
    regime=RegimeResult(
        trend=MarketRegime.TRENDING,
        volatility=MarketRegime.LOW_VOLATILITY,
        liquidity=MarketRegime.HIGH_LIQUIDITY,
    ),
    score=MarketScore(
        trend=90,
        volatility=70,
        liquidity=80,
        confidence=85,
        overall=0,
    ),
)

scorer = OverallScorer()

score = scorer.score(
    analysis
)

print(score)