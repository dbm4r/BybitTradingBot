from engine.engine_state import (
    EngineState,
)

from execution.framework.execution_pipeline_builder import (
    ExecutionPipelineBuilder,
)

from execution.services.exit_preparation_service import (
    ExitPreparationService,
)


class ExitExecutor:

    @staticmethod
    def execute(
        engine,
        timestamp,
        price,
        exit_reason,
    ):

        engine.state.set_state(
            EngineState.EXITING_POSITION,
        )

        context = (
            ExitPreparationService.prepare(
                engine=engine,
                timestamp=timestamp,
                price=price,
                exit_reason=exit_reason,
            )
        )

        pipeline = (
            ExecutionPipelineBuilder()
            .default_exit_pipeline()
            .build()
        )

        pipeline.execute(
            engine=engine,
            context=context,
        )

        engine.state.set_state(
            EngineState.READY,
        )