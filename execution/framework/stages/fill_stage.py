from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.execution_coordinator import (
    ExecutionCoordinator,
)


class FillStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        ExecutionCoordinator.process_entry(
            engine=engine,
            context=context,
        )

        return context