from execution.entry_executor import EntryExecutor
from execution.exit_executor import ExitExecutor


class ExecutionRouter:

    @staticmethod
    def execute(
        engine,
        order,
        row
    ):

        if order.side == "BUY":

            EntryExecutor.execute(
                engine=engine,
                timestamp=row["timestamp"],
                price=order.filled_price
            )

        else:

            ExitExecutor.execute(
                engine=engine,
                timestamp=row["timestamp"],
                price=order.filled_price,
                exit_reason="Limit Order"
            )