
from bybit.bybit_client import BybitClient
from live.live_runner import LiveRunner
from strategies.ema_crossover import EMACrossoverStrategy

from backtesting.execution_engine import ExecutionEngine
from backtesting.portfolio import Portfolio
from core.settings import Settings


client = BybitClient(
    api_key="xdRbOU4VvVZcwxOcEG",
    api_secret="s798S41QJlK10r3zcyPIWxD7p9Tjo70PNrpa",
    base_url="https://api-demo.bybit.com"
)

strategy = EMACrossoverStrategy()

settings = Settings()
settings.exchange = "PAPER"   # Keep paper trading for now

portfolio = Portfolio(
    initial_balance=settings.initial_balance
)

engine = ExecutionEngine(
    portfolio=portfolio,
    settings=settings,
    symbol="BTCUSDT",
    strategy=strategy
)

runner = LiveRunner(
    client=client,
    strategy=strategy,
    execution_engine=engine,
    symbol="BTCUSDT",
    interval=1
)

runner.run()