from datetime import datetime

from models.candle import Candle
from pipeline.trading_pipeline import TradingPipeline
from strategies.trend.sma_crossover import (
    SMACrossoverStrategy,
)

pipeline = TradingPipeline(
    strategy=SMACrossoverStrategy(
        fast_period=3,
        slow_period=5,
    ),
    symbol="BTCUSDT",
    interval="1",
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

    decision = pipeline.process_candle(
        candle
    )

print(decision.signal)
print(decision.strategy)
print(decision.reason)
print(decision.candle.close)
print(len(pipeline.candle_series))