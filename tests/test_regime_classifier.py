from core.config import Config
from data.data_manager import DataManager

from market.candle_factory import CandleFactory
from market.regime_classifier import RegimeClassifier

from models.candle_series import CandleSeries


config = Config()

manager = DataManager()

dataframe = manager.download_historical_data(
    symbol=config.symbol,
    interval=config.interval,
    limit=500,
)

series = CandleSeries(
    symbol=config.symbol,
    interval=config.interval,
)

for _, row in dataframe.iterrows():

    candle = CandleFactory.from_series(
        row=row,
        symbol=config.symbol,
        interval=config.interval,
    )

    series.add(candle)

classifier = RegimeClassifier()

result = classifier.classify(series)
print(result)

print("\n========== MARKET REGIME ==========\n")

print(f"Trend      : {result.trend.value}")
print(f"Volatility : {result.volatility.value}")
print(f"Liquidity  : {result.liquidity.value}")