from strategies.framework.base_strategy import BaseStrategy

from strategies.pipeline.strategy_pipeline import (
    StrategyPipeline,
)
from strategies.pipeline.strategy_stage import (
    StrategyStage,
)


class StrategyPipelineBuilder:

    def __init__(self):

        self._pipeline = StrategyPipeline()

    def add(
        self,
        strategy: BaseStrategy,
        *,
        enabled: bool = True,
        priority: int = 100,
    ):

        self._pipeline.add(
            StrategyStage(
                strategy=strategy,
                enabled=enabled,
                priority=priority,
            )
        )

        return self

    def add_many(
        self,
        *strategies: BaseStrategy,
    ):

        for strategy in strategies:

            self.add(
                strategy,
            )

        return self

    def build(
        self,
    ) -> StrategyPipeline:

        return self._pipeline