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

    @classmethod
    def analyze(
        cls,
        context,
        candles,
    ) -> MarketAnalysis:

        analyzer = cls()

        regime = analyzer.regime_classifier.classify(
            candles
        )

        score = MarketScore(
            trend=analyzer.trend_scorer.score(
                regime
            ),
            volatility=analyzer.volatility_scorer.score(
                regime
            ),
            liquidity=analyzer.liquidity_scorer.score(
                regime
            ),
            confidence=0.0,
            overall=0.0,
        )

        analysis = MarketAnalysis(
            regime=regime,
            score=score,
        )

        analysis.score.overall = (
            analyzer.overall_scorer.score(
                analysis
            )
        )

        return analysis