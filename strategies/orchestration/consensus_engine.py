from statistics import mean

from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)


class ConsensusEngine:
    """
    Produces a single decision from grouped strategy decisions.
    """

    def decide(
        self,
        grouped: dict[
            SignalType,
            tuple[StrategyDecision, ...],
        ],
    ) -> StrategyDecision:

        actionable = {
            signal: decisions
            for signal, decisions in grouped.items()
            if signal != SignalType.HOLD
        }

        candidates = actionable if actionable else grouped

        if not candidates:
            raise ValueError(
                "No strategy decisions available."
            )

        best_group = max(
            candidates.values(),
            key=lambda decisions: (
                len(decisions),
                mean(
                    decision.confidence
                    for decision in decisions
                ),
                max(
                    decision.confidence
                    for decision in decisions
                ),
            ),
        )

        return max(
            best_group,
            key=lambda decision: decision.confidence,
        )