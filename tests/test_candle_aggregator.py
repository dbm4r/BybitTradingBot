from core.config import Config
from data.data_manager import DataManager
from market.candle_aggregator import CandleAggregator
from market.candle_factory import CandleFactory


config = Config()

manager = DataManager()

dataframe = manager.download_historical_data(
    symbol=config.symbol,
    interval="1",
    limit=5,
)

candles = []

for _, row in dataframe.iterrows():

    candles.append(
        CandleFactory.from_series(
            row=row,
            symbol=config.symbol,
            interval="1",
        )
    )

aggregated = CandleAggregator.aggregate(
    candles=candles,
    interval="5",
)

print("========== CANDLE AGGREGATOR ==========\n")

print(f"Original Candles : {len(candles)}")
print()

print(f"Symbol           : {aggregated.symbol}")
print(f"Interval         : {aggregated.interval}")
print(f"Timestamp        : {aggregated.timestamp}")

print()

print(f"Open             : {aggregated.open}")
print(f"High             : {aggregated.high}")
print(f"Low              : {aggregated.low}")
print(f"Close            : {aggregated.close}")

print()

print(f"Volume           : {aggregated.volume}")
print(f"Turnover         : {aggregated.turnover}")