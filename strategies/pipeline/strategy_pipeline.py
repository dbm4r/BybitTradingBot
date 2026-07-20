from strategies.framework.strategy_context import (
    StrategyContext,
)
from strategies.framework.strategy_runner import (
    StrategyRunner,
)

from strategies.pipeline.pipeline_result import (
    PipelineResult,
)
from strategies.pipeline.strategy_stage import (
    StrategyStage,
)


class StrategyPipeline:

    def __init__(self):

        self._runner = StrategyRunner()

        self._stages: list[
            StrategyStage
        ] = []

    def add(
        self,
        stage: StrategyStage,
    ) -> None:

        self._stages.append(
            stage
        )

    def add_many(
        self,
        *stages: StrategyStage,
    ) -> None:

        self._stages.extend(
            stages
        )

    def run(
        self,
        context: StrategyContext,
    ) -> PipelineResult:

        result = PipelineResult()

        for stage in sorted(
            self._stages,
            key=lambda s: s.priority,
        ):

            if not stage.enabled:

                continue

            decision = stage.strategy.evaluate(
                context
            )

            result.add(
                decision
            )

        return result

    def clear(
        self,
    ) -> None:

        self._stages.clear()

    @property
    def count(
        self,
    ) -> int:

        return len(
            self._stages
        )

    @property
    def stages(
        self,
    ) -> tuple[
        StrategyStage,
        ...
    ]:

        return tuple(
            self._stages
        )