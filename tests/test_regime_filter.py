from market.market_regime import MarketRegime
from market.regime_filter import RegimeFilter
from market.regime_result import RegimeResult
from strategies.trend.ema_crossover import EMACrossover


strategy = EMACrossover(
    fast_period=9,
    slow_period=21,
)

regime_filter = RegimeFilter()

print("========== REGIME FILTER ==========\n")

# Should PASS
regime = RegimeResult(
    trend=MarketRegime.TRENDING,
    volatility=MarketRegime.LOW_VOLATILITY,
    liquidity=MarketRegime.HIGH_LIQUIDITY,
)

allowed, reason = regime_filter.allows(
    strategy=strategy,
    regime=regime,
)

print("Trending")
print(f"Allowed : {allowed}")
print(f"Reason  : {reason}")
print()

# Should FAIL
regime = RegimeResult(
    trend=MarketRegime.RANGING,
    volatility=MarketRegime.LOW_VOLATILITY,
    liquidity=MarketRegime.HIGH_LIQUIDITY,
)

allowed, reason = regime_filter.allows(
    strategy=strategy,
    regime=regime,
)

print("Ranging")
print(f"Allowed : {allowed}")
print(f"Reason  : {reason}")
print()

# Should FAIL
regime = RegimeResult(
    trend=MarketRegime.TRENDING,
    volatility=MarketRegime.LOW_VOLATILITY,
    liquidity=MarketRegime.LOW_LIQUIDITY,
)

allowed, reason = regime_filter.allows(
    strategy=strategy,
    regime=regime,
)

print("Low Liquidity")
print(f"Allowed : {allowed}")
print(f"Reason  : {reason}")