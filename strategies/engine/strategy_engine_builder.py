from strategies.framework.base_strategy import (
    BaseStrategy,
)

from strategies.engine.strategy_engine import (
    StrategyEngine,
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

from strategies.pipeline.strategy_pipeline_builder import (
    StrategyPipelineBuilder,
)


class StrategyEngineBuilder:

    def __init__(self):

        self._pipeline = (
            StrategyPipelineBuilder()
        )

        self._aggregator = (
            DecisionAggregator()
        )

        self._resolver = (
            ConflictResolver()
        )

        self._consensus = (
            ConsensusEngine()
        )

    def add(
        self,
        strategy: BaseStrategy,
        *,
        enabled: bool = True,
        priority: int = 100,
    ):

        self._pipeline.add(
            strategy,
            enabled=enabled,
            priority=priority,
        )

        return self

    def add_many(
        self,
        *strategies: BaseStrategy,
    ):

        self._pipeline.add_many(
            *strategies,
        )

        return self

    def aggregator(
        self,
        aggregator: DecisionAggregator,
    ):

        self._aggregator = aggregator

        return self

    def resolver(
        self,
        resolver: ConflictResolver,
    ):

        self._resolver = resolver

        return self

    def consensus(
        self,
        consensus: ConsensusEngine,
    ):

        self._consensus = consensus

        return self

    def build(
        self,
    ) -> StrategyEngine:

        return StrategyEngine(
            pipeline=self._pipeline.build(),
            aggregator=self._aggregator,
            resolver=self._resolver,
            consensus=self._consensus,
        )