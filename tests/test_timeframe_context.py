from core.config import Config
from data.data_manager import DataManager
from indicators.ema import ExponentialMovingAverage
from indicators.rsi import RelativeStrengthIndex
from market.candle_factory import CandleFactory
from market.timeframe import Timeframe
from market.timeframe_context import TimeframeContext
from models.candle_series import CandleSeries


config = Config()

manager = DataManager()

dataframe = manager.download_historical_data(
    symbol=config.symbol,
    interval="1",
    limit=100,
)

context = TimeframeContext(
    timeframe=Timeframe.M1.value,
    candles=CandleSeries(
        symbol=config.symbol,
        interval=Timeframe.M1.value,
    ),
)

context.add_indicators(
    ExponentialMovingAverage(9),
    RelativeStrengthIndex(14),
)

for _, row in dataframe.iterrows():

    candle = CandleFactory.from_series(
        row=row,
        symbol=config.symbol,
        interval=Timeframe.M1.value,
    )

    context.candles.add(candle)

context.calculate_indicators()

print("========== TIMEFRAME CONTEXT ==========\n")

print(
    f"Timeframe      : {context.timeframe}"
)

print(
    f"Candle Count   : {context.candles.count}"
)

print()

print(
    "Indicators:"
)

for name, result in context.indicators.items():

    print(
        f"{name:<10} Last = {result.last}"
    )