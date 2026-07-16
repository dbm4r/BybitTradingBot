from dataclasses import dataclass


@dataclass(slots=True)
class ScannerSettings:

    max_opportunities: int = 5

    minimum_score: float = 70.0

    trend_weight: float = 0.40

    liquidity_weight: float = 0.35

    volatility_weight: float = 0.25