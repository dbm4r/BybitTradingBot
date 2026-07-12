from datetime import datetime

from indicators.rsi import RSI
from models.candle import Candle
from models.candle_series import CandleSeries


series = CandleSeries(
    symbol="BTCUSDT",
    interval="1",
)

prices = [
    44,
    44.15,
    43.9,
    44.35,
    44.8,
    45.1,
    45.4,
    45.0,
    45.6,
    46.0,
    46.3,
    46.1,
    46.5,
    47.0,
    47.4,
    47.2,
    47.8,
    48.0,
    48.4,
    48.1,
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

rsi = RSI(14)

result = rsi.calculate(series)

print(result.name)
print(result.output_name)
print(result.parameters)
print(result.last)
print(result.values)