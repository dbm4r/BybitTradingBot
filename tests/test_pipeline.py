from datetime import datetime

from indicators.ema import ExponentialMovingAverage
from indicators.indicator_pipeline import IndicatorPipeline
from indicators.rsi import RSI
from indicators.sma import SimpleMovingAverage
from models.candle import Candle
from models.candle_series import CandleSeries


series = CandleSeries(
    symbol="BTCUSDT",
    interval="1",
)

prices = [
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100,
    110, 120, 130, 140, 150,
]

for price in prices:
    series.add(
        Candle(
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
    )

pipeline = IndicatorPipeline()

pipeline.add_many(
    SimpleMovingAverage(3),
    ExponentialMovingAverage(3),
    RSI(14),
)

results = pipeline.calculate(series)
indicator = pipeline.get("EMA_3")

print(indicator)

print(results.keys())

for name, result in results.items():
    print(name)
    print(result.last)

print(pipeline.has("EMA_3"))

print(pipeline.has("EMA_100"))
print(pipeline.count)

pipeline.remove("EMA_3")

print(pipeline.count)

print(pipeline.has("EMA_3"))