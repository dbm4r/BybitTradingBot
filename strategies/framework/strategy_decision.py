from dataclasses import dataclass

from models.candle import Candle
from strategies.framework.signal_type import SignalType


@dataclass(slots=True, frozen=True)
class StrategyDecision:

    signal: SignalType

    confidence: float

    reason: str

    strategy: str

    candle: Candle
    @classmethod
    def hold(
        cls,
        candle: Candle,
        strategy: str,
        reason: str,
    ) -> "StrategyDecision":

        return cls(
            signal=SignalType.HOLD,
            confidence=1.0,
            reason=reason,
            strategy=strategy,
            candle=candle,
        )