from core.settings import Settings
from backtesting.execution_engine import ExecutionEngine
from backtesting.portfolio import Portfolio
from strategies.trend.ema_crossover import (
    EMACrossover
)

settings = Settings()

settings.exchange = "BYBIT"

portfolio = Portfolio(
    settings.initial_balance
)

strategy = EMACrossover()

engine = ExecutionEngine(
    portfolio=portfolio,
    settings=settings,
    symbol="BTCUSDT",
    strategy=strategy,
    exchange_name="BYBIT"
)

engine.synchronizer.synchronize()
print()

print("========== ORDER MANAGER ==========")

print(
    f"Orders: {len(engine.order_manager.all_orders())}"
)

for order in engine.order_manager.all_orders():

    print(order)

print("===================================")
print()

print("\n========== PORTFOLIO ==========")
print(f"Cash: {engine.portfolio.cash:.2f}")

for symbol, position in engine.portfolio.positions.items():

    print(f"\nSymbol      : {symbol}")
    print(f"Quantity    : {position.quantity}")
    print(f"Entry Price : {position.entry_price}")

print("===============================")