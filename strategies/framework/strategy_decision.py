from dataclasses import dataclass

from strategies.framework.signal_type import SignalType


@dataclass(frozen=True)
class StrategyDecision:

    signal: SignalType

    confidence: float

    reason: str

    def __post_init__(self) -> None:

        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                "Confidence must be between 0.0 and 1.0."
            )

        if not self.reason.strip():
            raise ValueError(
                "Reason cannot be empty."
            )