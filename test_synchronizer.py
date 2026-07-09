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