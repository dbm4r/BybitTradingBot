from runtime.cycle.framework.base_cycle_stage import (
    BaseCycleStage,
)


class PreCycleStage(
    BaseCycleStage,
):

    def execute(
        self,
        context,
    ):

        """
        Future:
        - Synchronize exchange
        - Refresh balances
        - Refresh positions
        - Update market state
        """

        return context