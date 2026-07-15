from market.higher_timeframe_confirmation import HigherTimeframeConfirmation
from strategies.trend.ema_crossover import EMACrossoverStrategy
from strategies.trend.sma_crossover import SMACrossoverStrategy
from strategies.framework.strategy_context import StrategyContext
from models.candle_series import CandleSeries


print("========== HIGHER TIMEFRAME CONFIRMATION ==========\n")

# Strategy that does NOT require confirmation
sma = SMACrossoverStrategy(
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
ema = EMACrossoverStrategy(
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