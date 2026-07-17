from market.higher_timeframe_confirmation import HigherTimeframeConfirmation
from strategies.trend.ema_crossover import EMACrossover
from strategies.trend.sma_crossover import SMACrossover
from strategies.framework.strategy_context import StrategyContext
from models.candle_series import CandleSeries


print("========== HIGHER TIMEFRAME CONFIRMATION ==========\n")

# Strategy that does NOT require confirmation
sma = SMACrossover(
    fast_period=5,
    slow_period=20,
)

context = StrategyContext(
    candles=CandleSeries(
        symbol="BTCUSDT",
        interval="1",
    ),
    indicators={},
)

print(
    "SMA:",
    HigherTimeframeConfirmation.confirms(
        context=context,
        strategy=sma,
    ),
)

# Strategy that DOES require confirmation
ema = EMACrossover(
    fast_period=9,
    slow_period=21,
)

print(
    "EMA:",
    HigherTimeframeConfirmation.confirms(
        context=context,
        strategy=ema,
    ),
)