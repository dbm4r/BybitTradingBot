from core.config import Config
from data.data_manager import DataManager
from market.candle_factory import CandleFactory
from market.multi_timeframe_context import MultiTimeframeContext
from market.timeframe import Timeframe
from market.timeframe_context import TimeframeContext
from market.timeframe_synchronizer import TimeframeSynchronizer
from models.candle_series import CandleSeries


config = Config()

manager = DataManager()

# Download enough candles to cross a 5-minute boundary
dataframe = manager.download_historical_data(
    symbol=config.symbol,
    interval="1",
    limit=8,
)

context = MultiTimeframeContext(
    contexts={
        Timeframe.M5.value: TimeframeContext(
            timeframe=Timeframe.M5.value,
            candles=CandleSeries(
                symbol=config.symbol,
                interval=Timeframe.M5.value,
            ),
        ),
    },
)

synchronizer = TimeframeSynchronizer(
    context=context,
)

created_candles = []

for _, row in dataframe.iterrows():

    candle = CandleFactory.from_series(
        row=row,
        symbol=config.symbol,
        interval="1",
    )

    created = synchronizer.update(candle)

    created_candles.extend(created)

series = context.get(
    Timeframe.M5.value
).candles

print("========== TIMEFRAME SYNCHRONIZER ==========\n")

print(f"Input candles      : {len(dataframe)}")
print(f"Created candles    : {len(created_candles)}")
print(f"Stored candles     : {series.count}")

print()

for i, candle in enumerate(created_candles, start=1):

    print(f"----- Aggregated Candle #{i} -----")
    print(f"Timestamp : {candle.timestamp}")
    print(f"Interval  : {candle.interval}")
    print(f"Open      : {candle.open}")
    print(f"High      : {candle.high}")
    print(f"Low       : {candle.low}")
    print(f"Close     : {candle.close}")
    print(f"Volume    : {candle.volume}")
    print()