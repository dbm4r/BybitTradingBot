from market.market_regime import MarketRegime
from market.regime_result import RegimeResult

from scanner.market_analysis import MarketAnalysis
from scanner.scoring.market_score import MarketScore
from scanner.scoring.trend_scorer import TrendScorer


print("========== TREND SCORER ==========\n")


analysis = MarketAnalysis(
    regime=RegimeResult(
        trend=MarketRegime.TRENDING,
        volatility=MarketRegime.LOW_VOLATILITY,
        liquidity=MarketRegime.HIGH_LIQUIDITY,
    ),
    score=MarketScore(),
)


scorer = TrendScorer()


print(
    scorer.score(
        analysis.regime
    )
)