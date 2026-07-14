from datetime import datetime

import pandas as pd

from market.candle_factory import CandleFactory


row = pd.Series(
    {
        "timestamp": datetime.now(),
        "open": 100,
        "high": 110,
        "low": 95,
        "close": 105,
        "volume": 250,
        "turnover": 26250,
    }
)

candle = CandleFactory.from_series(
    row=row,
    symbol="BTCUSDT",
    interval="1",
)

assert candle.symbol == "BTCUSDT"
assert candle.interval == "1"

assert candle.open == 100
assert candle.high == 110
assert candle.low == 95
assert candle.close == 105

assert candle.volume == 250
assert candle.turnover == 26250

print("✓ CandleFactory from_series passed")
data = {
    "timestamp": datetime.now(),
    "open": 200,
    "high": 220,
    "low": 190,
    "close": 210,
    "volume": 100,
    "turnover": 21000,
}

candle = CandleFactory.from_dict(
    data=data,
    symbol="ETHUSDT",
    interval="5",
)

assert candle.symbol == "ETHUSDT"
assert candle.interval == "5"

assert candle.open == 200
assert candle.high == 220
assert candle.low == 190
assert candle.close == 210

print("✓ CandleFactory from_dict passed")
data = {
    "start": "1752400000000",
    "open": "300",
    "high": "320",
    "low": "295",
    "close": "315",
    "volume": "500",
    "turnover": "157500",
}

candle = CandleFactory.from_bybit(
    data=data,
    symbol="BTCUSDT",
    interval="1",
)

assert candle.symbol == "BTCUSDT"

assert candle.open == 300
assert candle.high == 320
assert candle.low == 295
assert candle.close == 315

print("✓ CandleFactory from_bybit passed")