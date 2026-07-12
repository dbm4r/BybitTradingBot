from models.candle import Candle
from models.candle_series import CandleSeries
from datetime import datetime


series = CandleSeries()

series.add(
    Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(),
        open=100,
        high=105,
        low=95,
        close=103,
        volume=120,
        turnover=12360,
    )
)

series.add(
    Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(),
        open=103,
        high=110,
        low=101,
        close=108,
        volume=140,
        turnover=15120,
    )
)

print(series.count)
print(series.first.close)
print(series.last.close)
print(series.close_prices)
print(series.high_prices)
print(series.candles)

for candle in series:
    print(candle.close)