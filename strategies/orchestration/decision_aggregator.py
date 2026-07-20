from strategies.framework.strategy_decision import (
    StrategyDecision,
)
from strategies.pipeline.pipeline_result import (
    PipelineResult,
)


class DecisionAggregator:
    """
    Collects every decision produced by the strategy pipeline.
    """

    def aggregate(
        self,
        result: PipelineResult,
    ) -> tuple[StrategyDecision, ...]:

        return tuple(
            result.decisions
        )