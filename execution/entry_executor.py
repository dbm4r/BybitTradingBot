from execution.framework.execution_pipeline_builder import (
    ExecutionPipelineBuilder,
)

from engine.engine_state import (
    EngineState,
)
from execution.services.entry_preparation_service import EntryPreparationService


class EntryExecutor:

    @staticmethod
    def execute(
        engine,
        decision,
    ):

        engine.state.set_state(
            EngineState.PLACING_ORDER,
        )

        context = (
            EntryPreparationService.prepare(
                engine=engine,
                decision=decision,
            )
        )

        engine.total_fees += (
            context.fee
        )

        pipeline = (
            ExecutionPipelineBuilder()
            .default_entry_pipeline()
            .build()
        )

        pipeline.execute(
            engine=engine,
            context=context,
        )

        engine.state.set_state(
            EngineState.READY,
        )