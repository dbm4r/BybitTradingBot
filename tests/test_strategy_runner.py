from datetime import datetime

from models.candle import Candle
from models.candle_series import CandleSeries
from strategies.trend.sma_crossover import SMACrossover
from strategies.framework.strategy_runner import StrategyRunner


series = CandleSeries(
    symbol="BTCUSDT",
    interval="1",
)

prices = [
    100,
    105,
    110,
    115,
    120,
    125,
    130,
    135,
    140,
    145,
    150,
]

for price in prices:

    series.add(
        Candle(
            symbol="BTCUSDT",
            interval="1",
            timestamp=datetime.now(),
            open=price,
            high=price,
            low=price,
            close=price,
            volume=1,
            turnover=price,
        )
    )

strategy = SMACrossover(
    fast_period=3,
    slow_period=5,
)

runner = StrategyRunner()

decision = runner.run(
    strategy,
    series,
)

print(decision.signal)
print(decision.confidence)
print(decision.reason)
print(decision.strategy)
print(decision.candle.timestamp)
print(decision.candle.close)