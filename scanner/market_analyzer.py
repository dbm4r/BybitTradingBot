from market.regime_classifier import RegimeClassifier

from scanner.market_analysis import MarketAnalysis
from scanner.scoring.market_score import MarketScore
from scanner.scoring.trend_scorer import TrendScorer
from scanner.scoring.volatility_scorer import VolatilityScorer
from scanner.scoring.liquidity_scorer import LiquidityScorer
from scanner.scoring.overall_scorer import OverallScorer


class MarketAnalyzer:

    def __init__(
        self,
        regime_classifier=None,
    ):

        self.regime_classifier = (
            regime_classifier
            or RegimeClassifier()
        )

        self.trend_scorer = TrendScorer()
        self.volatility_scorer = VolatilityScorer()
        self.liquidity_scorer = LiquidityScorer()
        self.overall_scorer = OverallScorer()

    def analyze(
        self,
        context,
        candles,
    ) -> MarketAnalysis:

        regime = self.regime_classifier.classify(
            candles
        )

        score = MarketScore(
            trend=self.trend_scorer.score(
                regime
            ),
            volatility=self.volatility_scorer.score(
                regime
            ),
            liquidity=self.liquidity_scorer.score(
                regime
            ),
            confidence=0.0,
            overall=0.0,
        )

        analysis = MarketAnalysis(
            regime=regime,
            score=score,
        )

        analysis.score.overall = self.overall_scorer.score(
            analysis
        )

        return analysis