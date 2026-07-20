from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)


class ConflictResolver:
    """
    Groups strategy decisions by signal type.
    """

    def resolve(
        self,
        decisions: tuple[StrategyDecision, ...],
    ) -> dict[
        SignalType,
        tuple[StrategyDecision, ...],
    ]:

        grouped: dict[
            SignalType,
            list[StrategyDecision],
        ] = {}

        for decision in decisions:

            grouped.setdefault(
                decision.signal,
                [],
            ).append(
                decision,
            )

        return {
            signal: tuple(items)
            for signal, items in grouped.items()
        }