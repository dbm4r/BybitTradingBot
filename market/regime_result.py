from dataclasses import dataclass

from market.market_regime import MarketRegime


@dataclass(slots=True)
class RegimeResult:

    trend: MarketRegime

    volatility: MarketRegime

    liquidity: MarketRegime