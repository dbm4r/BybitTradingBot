from models.candle import Candle

sample = {
    "start": 1752300000000,
    "open": "108500",
    "high": "108900",
    "low": "108300",
    "close": "108700",
    "volume": "145.8",
    "turnover": "15849320",
}

candle = Candle.from_bybit("BTCUSDT", "1", sample)

print(candle)
print(candle.is_bullish)
print(candle.body_size)
print(candle.range)