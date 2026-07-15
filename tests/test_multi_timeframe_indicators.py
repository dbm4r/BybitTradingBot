from core.config import Config
from data.data_manager import DataManager
from indicators.ema import ExponentialMovingAverage
from indicators.rsi import RelativeStrengthIndex
from market.candle_factory import CandleFactory
from market.multi_timeframe_context import MultiTimeframeContext
from market.timeframe import Timeframe
from market.timeframe_context import TimeframeContext
from market.timeframe_synchronizer import TimeframeSynchronizer
from models.candle_series import CandleSeries


config = Config()

manager = DataManager()

dataframe = manager.download_historical_data(
    symbol=config.symbol,
    interval="1",
    limit=100,
)

m5 = TimeframeContext(
    timeframe=Timeframe.M5.value,
    candles=CandleSeries(
        symbol=config.symbol,
        interval=Timeframe.M5.value,
    ),
)

m5.add_indicators(
    ExponentialMovingAverage(9),
    RelativeStrengthIndex(14),
)

context = MultiTimeframeContext(
    contexts={
        Timeframe.M5.value: m5,
    }
)

synchronizer = TimeframeSynchronizer(
    context=context,
)

for _, row in dataframe.iterrows():

    candle = CandleFactory.from_series(
        row=row,
        symbol=config.symbol,
        interval="1",
    )

    synchronizer.update(
        candle,
    )

m5 = context.get(
    Timeframe.M5.value
)

print("========== MULTI TIMEFRAME INDICATORS ==========\n")

print(
    f"5m candles : {m5.candles.count}"
)

print()

for name, result in m5.indicators.items():

    print(
        f"{name:<10} Count={result.count:<4} Last={result.last}"
    )