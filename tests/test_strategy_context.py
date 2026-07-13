from datetime import datetime

from models.candle import Candle
from models.candle_series import CandleSeries
from models.indicator_result import IndicatorResult
from strategies.strategy_context import StrategyContext


series = CandleSeries(
    symbol="BTCUSDT",
    interval="1",
)

series.add(
    Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(),
        open=100,
        high=110,
        low=95,
        close=105,
        volume=100,
        turnover=10500,
    )
)

context = StrategyContext(
    candles=series,
    indicators={
        "EMA_20": IndicatorResult(
            name="EMA",
            output_name="EMA_20",
            values=[100.5],
            parameters={
                "period": 20,
            },
        )
    },
)

print(context.candles.symbol)
print(context.candles.interval)
print(context.candles.last.close)

indicator = context.get_indicator("EMA_20")

print(indicator.last if indicator else None)

print(context.get_indicator("RSI_14"))