from dataclasses import dataclass, field

from strategies.framework.strategy_decision import (
    StrategyDecision,
)


@dataclass(slots=True)
class PipelineResult:
    """
    Result produced by the strategy pipeline.
    """

    decisions: list[StrategyDecision] = field(
        default_factory=list,
    )

    def add(
        self,
        decision: StrategyDecision,
    ) -> None:

        self.decisions.append(
            decision
        )

    @property
    def count(
        self,
    ) -> int:

        return len(
            self.decisions
        )

    @property
    def empty(
        self,
    ) -> bool:

        return self.count == 0