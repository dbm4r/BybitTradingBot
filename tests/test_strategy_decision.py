from strategies.signal_type import SignalType
from strategies.strategy_decision import StrategyDecision


decision = StrategyDecision(
    signal=SignalType.OPEN_LONG,
    confidence=1.0,
    reason="EMA crossed SMA",
)

print(decision.signal)

print(decision.confidence)

print(decision.reason)