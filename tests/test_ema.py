from datetime import datetime

from indicators.ema import ExponentialMovingAverage
from models.candle import Candle
from models.candle_series import CandleSeries


series = CandleSeries(
    symbol="BTCUSDT",
    interval="1",
)

prices = [10, 20, 30, 40, 50]

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

ema = ExponentialMovingAverage(3)

result = ema.calculate(series)

print(result.name)
print(result.output_name)
print(result.parameters)
print(result.last)
print(result.values)