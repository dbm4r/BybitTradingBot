from datetime import datetime

from models.candle import Candle
from pipeline.trading_pipeline import TradingPipeline
from sessions.trading_session import TradingSession
from strategies.trend.sma_crossover import (
    SMACrossoverStrategy,
)


class DummyEngine:

    def process_decision(
        self,
        decision,
    ):

        print(decision.signal)
        print(decision.strategy)
        print(decision.reason)
        print(decision.candle.close)


pipeline = TradingPipeline(
    strategy=SMACrossoverStrategy(
        fast_period=3,
        slow_period=5,
    ),
    symbol="BTCUSDT",
    interval="1",
)

session = TradingSession(
    engine=DummyEngine(),
    pipeline=pipeline,
)

prices = [
    100,
    105,
    110,
    115,
    120,
    125,
]

for price in prices:

    candle = Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(),
        open=price,
        high=price,
        low=price,
        close=price,
        volume=1,
        turnover=price,
    )

    session.process_candle(
        candle
    )