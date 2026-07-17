from core.settings import Settings
from backtesting.portfolio import Portfolio
from backtesting.execution_engine import ExecutionEngine

from bybit.bybit_client import BybitClient

from live.live_runner import LiveRunner

from strategies.trend.ema_crossover import EMACrossover


settings = Settings()

portfolio = Portfolio(
    initial_balance=settings.initial_balance
)

strategy = EMACrossover(
    fast_period=20,
    slow_period=50
)

engine = ExecutionEngine(
    portfolio=portfolio,
    settings=settings,
    symbol="BTCUSDT",
    strategy=strategy,
    exchange_name="BYBIT"
)

client = BybitClient(
    api_key=settings.api_key,
    api_secret=settings.api_secret,
    base_url=settings.base_url
)

runner = LiveRunner(
    client=client,
    strategy=strategy,
    execution_engine=engine,
    symbol="BTCUSDT",
    interval=1
)

runner.run()