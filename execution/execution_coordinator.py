from execution.fill_processor import (
    FillProcessor,
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

        ExecutionCoordinator._validate_exchange_result(
            context.exchange_result,
        )

        ExecutionCoordinator._assign_exchange_order_id(
            order=context.order,
            exchange_result=context.exchange_result,
        )

        engine.execution_state.register_pending_order(
            context.order,
        )

        FillProcessor.process_exit_fill(
            engine=engine,
            order=context.order,
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