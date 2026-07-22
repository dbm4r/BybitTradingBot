from execution.fill_processor import (
    FillProcessor,
)

from execution.services.exit_order_request_factory import (
    ExitOrderRequestFactory,
)

from execution.services.order_submission_service import (
    OrderSubmissionService,
)


class ExecutionCoordinator:

    @staticmethod
    def process_entry(
        engine,
        context,
    ):

        ExecutionCoordinator._validate_exchange_result(
            context.exchange_result,
        )

        ExecutionCoordinator._assign_exchange_order_id(
            order=context.order,
            exchange_result=context.exchange_result,
        )

        FillProcessor.process_entry_fill(
            engine=engine,
            context=context,
        )

    @staticmethod
    def process_exit(
        engine,
        context,
    ):

        order = ExitOrderRequestFactory.create(
            engine=engine,
            context=context,
            timestamp=context.timestamp,
        )

        exchange_result = (
            OrderSubmissionService.submit(
                engine=engine,
                order=order,
            )
        )

        ExecutionCoordinator._validate_exchange_result(
            exchange_result,
        )

        ExecutionCoordinator._assign_exchange_order_id(
            order=order,
            exchange_result=exchange_result,
        )

        engine.execution_state.pending_orders[
            order.exchange_order_id
        ] = order

        FillProcessor.process_exit_fill(
            engine=engine,
            order=order,
            timestamp=context.timestamp,
            price=context.entry_price,
            exit_reason=context.exit_reason,
        )

    @staticmethod
    def _validate_exchange_result(
        exchange_result,
    ):

        if not exchange_result.success:

            raise RuntimeError(
                exchange_result.error,
            )

    @staticmethod
    def _assign_exchange_order_id(
        order,
        exchange_result,
    ):

        order.exchange_order_id = (
            exchange_result.order.order_id
        )