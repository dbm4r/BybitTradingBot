from execution.fill_processor import FillProcessor

class ExecutionCoordinator:

    @staticmethod
    def process_entry(
        engine,
        context,
    ):

        if not context.exchange_result.success:
            raise RuntimeError(
                context.exchange_result.error
            )

        context.order.exchange_order_id = (
            context.exchange_result.order.order_id
        )

        FillProcessor.process_entry_fill(
            engine=engine,
            context=context,
        )

    @staticmethod
    def process_exit(
        engine,
        order,
        exchange_result,
        timestamp,
        price,
        exit_reason
    ):

        if not exchange_result.success:
            raise RuntimeError(
                exchange_result.error
            )

        order.exchange_order_id = (
            exchange_result.order.order_id
        )
        engine.execution_state.pending_orders[
            order.exchange_order_id
        ] = order

        FillProcessor.process_exit_fill(
            engine=engine,
            order=order,
            timestamp=timestamp,
            price=price,
            exit_reason=exit_reason
        )