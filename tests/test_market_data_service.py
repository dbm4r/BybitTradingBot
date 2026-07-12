from datetime import datetime

from market.market_data_service import MarketDataService
from models.candle import Candle


market = MarketDataService()

candle = Candle(
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

market.add_candle(candle)

series = market.get_series("BTCUSDT", "1")

print(series.count)
print(market.get_last_candle("BTCUSDT", "1"))
print(market.get_close_prices("BTCUSDT", "1"))