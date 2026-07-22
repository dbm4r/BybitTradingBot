from execution.framework.base_executor import (
    BaseExecutor,
)


class ExecutionPipeline:

    def __init__(
        self,
        stages: list[BaseExecutor],
    ):

        self._stages = list(stages)

    def execute(
        self,
        engine,
        context,
    ):

        current = context

        for stage in self._stages:

            current = stage.execute(
                engine,
                current,
            )

            if not current.continue_execution:

                break

        return current

    @property
    def stages(
        self,
    ):

        return tuple(
            self._stages
        )