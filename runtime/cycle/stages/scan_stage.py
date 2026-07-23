from runtime.cycle.framework.base_cycle_stage import (
    BaseCycleStage,
)


class ScanStage(
    BaseCycleStage,
):

    def execute(
        self,
        context,
    ):

        context.opportunities = (
            context.scanner.scan()
        )

        return context