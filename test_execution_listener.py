from core.settings import Settings
from backtesting.portfolio import Portfolio
from backtesting.execution_engine import ExecutionEngine
from strategies.ema_crossover import EMACrossoverStrategy

settings = Settings()
settings.exchange = "PAPER"

portfolio = Portfolio(settings.initial_balance)

strategy = EMACrossoverStrategy()

engine = ExecutionEngine(
    portfolio=portfolio,
    settings=settings,
    symbol="BTCUSDT",
    strategy=strategy
)

print(
    engine.execution_listener.poll()
)