from market.market_regime import MarketRegime
from market.regime_result import RegimeResult
from scanner.market_analysis import MarketAnalysis
from scanner.scoring.market_score import MarketScore


print("========== MARKET ANALYSIS ==========\n")


result = RegimeResult(
    trend=MarketRegime.TRENDING,
    volatility=MarketRegime.LOW_VOLATILITY,
    liquidity=MarketRegime.LOW_LIQUIDITY,
)


analysis = MarketAnalysis(
    regime=result,
    score=MarketScore(
        trend=90,
        volatility=70,
        liquidity=60,
        confidence=80,
    ),
)


print(analysis.score.trend)
print(analysis.score.volatility)
print(analysis.score.liquidity)
print(analysis.score.confidence)
print(analysis.score.overall)