from scanner.market_analysis import MarketAnalysis
from scanner.scanner_settings import ScannerSettings
from scanner.scoring.base_scorer import BaseScorer


class OverallScorer(BaseScorer):

    def __init__(
        self,
        settings: ScannerSettings | None = None,
    ):

        self.settings = (
            settings
            or ScannerSettings()
        )

    def score(
        self,
        analysis: MarketAnalysis,
    ) -> float:

        score = analysis.score

        return (
            score.trend * self.settings.trend_weight
            + score.liquidity * self.settings.liquidity_weight
            + score.volatility * self.settings.volatility_weight
        )