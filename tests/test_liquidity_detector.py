from core.config import Config
from data.data_manager import DataManager
from market.candle_factory import CandleFactory
from market.liquidity_detector import LiquidityDetector
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

    series.add(
        CandleFactory.from_series(
            row=row,
            symbol=config.symbol,
            interval=config.interval,
        )
    )

detector = LiquidityDetector()

result = detector.detect(series)

print(result)