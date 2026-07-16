from market.multi_timeframe_context import MultiTimeframeContext
from market.timeframe import Timeframe
from market.timeframe_context import TimeframeContext
from models.candle_series import CandleSeries
from models.candle import Candle

from scanner.market_analyzer import MarketAnalyzer


print("========== MARKET ANALYZER ==========\n")


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


series.add(
    Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=2,
        open=104,
        high=108,
        low=103,
        close=107,
        volume=1200,
        turnover=128400,
    )
)


context = MultiTimeframeContext(
    contexts={
        Timeframe.M1.value: TimeframeContext(
            timeframe=Timeframe.M1.value,
            candles=series,
        )
    }
)


analysis = MarketAnalyzer.analyze(
    context=context,
    candles=series,
)


print("Regime:")
print(analysis.regime)

print()

print("Trend Score:")
print(analysis.trend_score)

print()

print("Volatility Score:")
print(analysis.volatility_score)

print()

print("Liquidity Score:")
print(analysis.liquidity_score)

print()

print("Confidence:")
print(analysis.confidence)