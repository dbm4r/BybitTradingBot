from strategies.strategy_factory import StrategyFactory

strategy = StrategyFactory.create(
    "SMA",
    fast_period=20,
    slow_period=50,
)

print(type(strategy))
print(strategy.name)
print(strategy.parameters)