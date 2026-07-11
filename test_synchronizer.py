from core.settings import Settings
from backtesting.execution_engine import ExecutionEngine
from backtesting.portfolio import Portfolio
from strategies.ema_crossover import (
    EMACrossoverStrategy
)

settings = Settings()

settings.exchange = "BYBIT"

portfolio = Portfolio(
    settings.initial_balance
)

strategy = EMACrossoverStrategy()

engine = ExecutionEngine(
    portfolio=portfolio,
    settings=settings,
    symbol="BTCUSDT",
    strategy=strategy
)

engine.synchronizer.synchronize()
print()

print("========== PORTFOLIO ==========")

print(
    f"Cash: {engine.portfolio.cash:.2f}"
)

position = engine.portfolio.get_position(
    "BTCUSDT"
)

print(
    f"Symbol      : {position.symbol}"
)

print(
    f"Quantity    : {position.quantity}"
)

print(
    f"Entry Price : {position.entry_price}"
)

print("===============================")