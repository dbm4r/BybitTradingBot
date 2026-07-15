from market.market_regime import MarketRegime
from market.regime_filter import RegimeFilter
from market.regime_result import RegimeResult
from strategies.framework.strategy_factory import StrategyFactory

strategy = StrategyFactory.create("EMA")

regime = RegimeResult(
    trend=MarketRegime.TRENDING,
    volatility=MarketRegime.LOW_VOLATILITY,
    liquidity=MarketRegime.HIGH_LIQUIDITY,
)

filter = RegimeFilter()

allowed = filter.allows(
    decision=None,
    regime=regime,
)

print(f"Allowed: {allowed}")