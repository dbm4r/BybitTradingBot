from strategies.framework.strategy_context import (
    StrategyContext,
)
from strategies.framework.strategy_decision import (
    StrategyDecision,
)

from strategies.orchestration.consensus_engine import (
    ConsensusEngine,
)
from strategies.orchestration.conflict_resolver import (
    ConflictResolver,
)
from strategies.orchestration.decision_aggregator import (
    DecisionAggregator,
)

from strategies.pipeline.strategy_pipeline import (
    StrategyPipeline,
)


class StrategyEngine:
    """
    High-level façade for multi-strategy evaluation.
    """

    def __init__(
        self,
        pipeline: StrategyPipeline,
        aggregator: DecisionAggregator,
        resolver: ConflictResolver,
        consensus: ConsensusEngine,
    ):

        self.pipeline = pipeline
        self.aggregator = aggregator
        self.resolver = resolver
        self.consensus = consensus

    def evaluate(
        self,
        context: StrategyContext,
    ) -> StrategyDecision:

        pipeline_result = self.pipeline.run(
            context,
        )

        decisions = self.aggregator.aggregate(
            pipeline_result,
        )

        grouped = self.resolver.resolve(
            decisions,
        )

        return self.consensus.decide(
            grouped,
        )