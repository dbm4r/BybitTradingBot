import asyncio

from core.settings import Settings

from backtesting.portfolio import Portfolio
from backtesting.execution_engine import ExecutionEngine

from bybit.bybit_client import BybitClient

from live.candle_provider import CandleProvider
from live.websocket_runner import WebSocketRunner

from strategies.trend.ema_crossover import EMACrossoverStrategy


settings = Settings()

client = BybitClient(
    api_key=settings.api_key,
    api_secret=settings.api_secret,
    base_url=settings.base_url
)

provider = CandleProvider(client)

provider.initialize(
    symbol="BTCUSDT",
    interval="1",
    limit=200
)

strategy = EMACrossoverStrategy(
    fast_period=20,
    slow_period=50
)

portfolio = Portfolio(
    initial_balance=settings.initial_balance
)

engine = ExecutionEngine(
    portfolio=portfolio,
    settings=settings,
    symbol="BTCUSDT",
    strategy=strategy,
    exchange_name="BYBIT"
)


async def candle_received(candle):

    dataframe = provider.append_candle(candle)

    if dataframe is None:
        return

    dataframe = strategy.generate_signals(
        dataframe
    )

    row = dataframe.iloc[-1]

    print("\n========== NEW CANDLE ==========")
    print(row[[
        "timestamp",
        "close",
        "signal"
    ]])
    print("===============================\n")

    engine.process_candle(row)


runner = WebSocketRunner(
    symbol="BTCUSDT",
    interval="1"
)

runner.socket.on_candle = candle_received

asyncio.run(
    runner.run()
)