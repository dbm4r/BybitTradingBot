from dataclasses import dataclass
from scanner.scoring.market_score import MarketScore
from market.regime_result import RegimeResult


@dataclass(slots=True)
class MarketAnalysis:

    regime: RegimeResult

    score: MarketScore