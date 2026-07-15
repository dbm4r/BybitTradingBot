from market.multi_timeframe_context import MultiTimeframeContext
from market.timeframe import Timeframe
from market.timeframe_context import TimeframeContext
from models.candle_series import CandleSeries


m1 = TimeframeContext(
    timeframe=Timeframe.M1.value,
    candles=CandleSeries(
        symbol="BTCUSDT",
        interval="1",
    ),
)

h1 = TimeframeContext(
    timeframe=Timeframe.H1.value,
    candles=CandleSeries(
        symbol="BTCUSDT",
        interval="60",
    ),
)

d1 = TimeframeContext(
    timeframe=Timeframe.D1.value,
    candles=CandleSeries(
        symbol="BTCUSDT",
        interval="D",
    ),
)

context = MultiTimeframeContext(
    contexts={
        Timeframe.M1.value: m1,
        Timeframe.H1.value: h1,
        Timeframe.D1.value: d1,
    }
)

print("========== MULTI TIMEFRAME CONTEXT ==========\n")

print(context.get(Timeframe.M1.value).timeframe)
print(context.get(Timeframe.H1.value).timeframe)
print(context.get(Timeframe.D1.value).timeframe)

print()

print(context.get(Timeframe.M1.value).candles.symbol)
print(context.get(Timeframe.H1.value).candles.symbol)
print(context.get(Timeframe.D1.value).candles.symbol)

print()

print(context.get(Timeframe.M1.value).candles.interval)
print(context.get(Timeframe.H1.value).candles.interval)
print(context.get(Timeframe.D1.value).candles.interval)