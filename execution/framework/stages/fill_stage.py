from execution.execution_coordinator import (
    ExecutionCoordinator,
)

from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.models.execution_type import (
    ExecutionType,
)


class FillStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        if (
            context.execution_type
            is ExecutionType.ENTRY
        ):

            ExecutionCoordinator.process_entry(
                engine=engine,
                context=context,
            )

        else:

            ExecutionCoordinator.process_exit(
                engine=engine,
                context=context,
            )

        return context