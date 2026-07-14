import asyncio
from pipeline.trading_pipeline import TradingPipeline
from trading.trading_session import TradingSession
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

history = provider.initialize(
    symbol="BTCUSDT",
    interval="1",
    limit=200,
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
pipeline = TradingPipeline(
    strategy=strategy,
    symbol="BTCUSDT",
    interval="1",
)

history = provider.initialize(
    symbol="BTCUSDT",
    interval="1",
    limit=200,
)

pipeline.load_history(history)

session = TradingSession(
    engine=engine,
    pipeline=pipeline,
)


async def candle_received(candle):

    candle = provider.append_candle(candle)

    if candle is None:
        return

    decision = session.process_candle(
        candle
    )

    print("\n========== NEW CANDLE ==========")
    print(decision)
    print("===============================\n")