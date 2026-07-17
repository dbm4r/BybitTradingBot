from portfolio.portfolio_manager import PortfolioManager
from strategies.trend.sma_crossover import SMACrossover


manager = PortfolioManager()

manager.register_asset(
    symbol="BTCUSDT",
    strategy=SMACrossover(
        fast_period=5,
        slow_period=20,
    ),
)

manager.register_asset(
    symbol="ETHUSDT",
    strategy=SMACrossover(
        fast_period=5,
        slow_period=20,
    ),
)

manager.register_asset(
    symbol="SOLUSDT",
    strategy=SMACrossover(
        fast_period=5,
        slow_period=20,
    ),
)

print("========== PORTFOLIO MANAGER ==========\n")

print(f"Assets : {manager.count}")

print()

for symbol in manager.symbols:

    asset = manager.get_asset(symbol)

    print(f"Symbol   : {asset.symbol}")
    print(f"Strategy : {asset.strategy.name}")
    print()