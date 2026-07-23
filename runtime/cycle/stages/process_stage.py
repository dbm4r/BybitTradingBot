from runtime.cycle.framework.base_cycle_stage import (
    BaseCycleStage,
)


class ProcessStage(
    BaseCycleStage,
):

    def execute(
        self,
        context,
    ):

        context.processor.process(
            context.opportunities,
        )

        return context