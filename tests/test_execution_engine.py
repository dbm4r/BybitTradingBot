from datetime import datetime

from models.candle import Candle
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)

candle = Candle(
    symbol="BTCUSDT",
    interval="1",
    timestamp=datetime.now(),
    open=100,
    high=105,
    low=99,
    close=104,
    volume=100,
    turnover=10400,
)

decision = StrategyDecision(
    signal=SignalType.OPEN_LONG,
    confidence=1.0,
    reason="Test Decision",
    strategy="Test Strategy",
    candle=candle,
)

print(decision.signal)
print(decision.strategy)
print(decision.reason)
print(decision.candle.close)