from dataclasses import dataclass

from market.regime_result import RegimeResult
from scanner.scoring.market_score import MarketScore


@dataclass(slots=True)
class MarketAnalysis:

    regime: RegimeResult

    score: MarketScore

    @property
    def trend_score(
        self,
    ) -> float:

        return self.score.trend

    @property
    def volatility_score(
        self,
    ) -> float:

        return self.score.volatility

    @property
    def liquidity_score(
        self,
    ) -> float:

        return self.score.liquidity

    @property
    def confidence_score(
        self,
    ) -> float:

        return self.score.confidence

    @property
    def overall_score(
        self,
    ) -> float:

        return self.score.overall