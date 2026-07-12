from datetime import datetime

from indicators.sma import SimpleMovingAverage
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

sma = SimpleMovingAverage(3)

result = sma.calculate(series)

print(result.name)
print(result.output_name)
print(result.last)
print(result.count)
print(result.is_empty)
print(result.values)