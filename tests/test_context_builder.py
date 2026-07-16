from scanner.context_builder import ContextBuilder
from models.candle_series import CandleSeries
from models.candle import Candle

print("========== CONTEXT BUILDER ==========\n")

series = CandleSeries(
    symbol="BTCUSDT",
    interval="1",
)

series.add(
    Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=1,
        open=100,
        high=105,
        low=99,
        close=104,
        volume=1000,
        turnover=104000,
    )
)

context = ContextBuilder.build(
    series
)

print(
    context.get("1").timeframe
)

print(
    context.get("1").candles.symbol
)

print(
    len(
        context.get("1").candles
    )
)