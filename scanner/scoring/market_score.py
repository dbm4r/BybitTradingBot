from dataclasses import dataclass


@dataclass(slots=True)
class MarketScore:

    trend: float = 0.0

    volatility: float = 0.0

    liquidity: float = 0.0

    confidence: float = 0.0

    overall: float = 0.0