from models.candle import Candle
from execution.entry_executor import EntryExecutor
from execution.exit_executor import ExitExecutor


class ExecutionRouter:

    _handlers = {
        "BUY": EntryExecutor.execute,
        "SELL": ExitExecutor.execute,
    }

    @classmethod
    def execute(
        cls,
        engine,
        order,
        candle: Candle,
    ):

        handler = cls._handlers.get(order.side)

        if handler is None:
            raise ValueError(
                f"Unsupported order side: {order.side}"
            )

        if order.side == "SELL":

            handler(
                engine=engine,
                timestamp=candle.timestamp,
                price=order.filled_price,
                exit_reason="Limit Order",
            )

        else:

            handler(
                engine=engine,
                timestamp=candle.timestamp,
                price=order.filled_price,
            )