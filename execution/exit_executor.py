from engine.engine_state import (
    EngineState,
)

from execution.execution_coordinator import (
    ExecutionCoordinator,
)

from execution.services.exit_preparation_service import (
    ExitPreparationService,
)

from execution.services.exit_order_request_factory import (
    ExitOrderRequestFactory,
)

from execution.services.order_submission_service import (
    OrderSubmissionService,
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
            EngineState.EXITING_POSITION
        )

        context = (
            ExitPreparationService.prepare(
                engine=engine,
                timestamp=timestamp,
                price=price,
                exit_reason=exit_reason,
            )
        )

        order = (
            ExitOrderRequestFactory.create(
                engine=engine,
                context=context,
                timestamp=timestamp,
            )
        )

        result = (
            OrderSubmissionService.submit(
                engine=engine,
                order=order,
            )
        )

        ExecutionCoordinator.process_exit(
            engine=engine,
            order=order,
            exchange_result=result,
            timestamp=timestamp,
            price=context.entry_price,
            exit_reason=exit_reason,
        )

        engine.state.set_state(
            EngineState.READY
        )