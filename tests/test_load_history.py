from datetime import datetime

from models.candle import Candle
from models.candle_series import CandleSeries
from pipeline.trading_pipeline import TradingPipeline
from strategies.trend.sma_crossover import SMACrossover


series = CandleSeries(
    symbol="BTCUSDT",
    interval="1",
)

for i in range(60):

    series.add(
        Candle(
            symbol="BTCUSDT",
            interval="1",
            timestamp=datetime.now(),
            open=100 + i,
            high=101 + i,
            low=99 + i,
            close=100 + i,
            volume=100,
            turnover=10000,
        )
    )

pipeline = TradingPipeline(
    strategy=SMACrossover(),
    symbol="BTCUSDT",
    interval="1",
)

pipeline.load_history(series)

assert pipeline.candle_series.count == 60

print("✓ TradingPipeline load_history passed")