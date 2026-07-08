from orders.order_status import OrderStatus
from orders.order_status import OrderStatus
from execution.entry_executor import EntryExecutor
from execution.exit_executor import ExitExecutor
from execution.execution_router import ExecutionRouter
from orders.oco_manager import OCOManager

class OrderManager:

    def __init__(self):
        self.oco_manager = OCOManager()

        self.orders = []

    def submit(self, order):

        self.orders.append(order)

        print(f"Order Submitted : {order.side}")

        return order

    def fill(
        self,
        order,
        quantity,
        price,
        timestamp
    ):
        order.filled_price = price
        order.filled_time = timestamp

        order.filled_quantity += quantity

        order.remaining_quantity -= quantity

        if order.remaining_quantity <= 0:

            order.remaining_quantity = 0
            order.status = OrderStatus.FILLED

        else:

            order.status = OrderStatus.PARTIALLY_FILLED

        print(
            f"Order Filled : "
            f"{order.side} "
            f"{quantity:.6f} @ "
            f"{price:.2f}"
        )

        return order
    def all_orders(self):

        return self.orders
    def submit_pending(self, order):


        self.orders.append(order)

        print(
            f"Pending Limit Order @ {order.limit_price:.2f}"
        )

        return order
    def pending(self):

        return [
            order
            for order in self.orders
            if order.status == OrderStatus.PENDING
        ]
    def process_pending_orders(
        self,
        execution_engine,
        row
    ):

        for order in self.pending():
            if (
                order.expires_at is not None
                and row["timestamp"] >= order.expires_at
            ):

                order.expire()

                continue

            if not order.should_fill(row):
                continue

            self.fill(
                order,
                order.remaining_quantity,
                order.execution_price,
                row["timestamp"]
            )

            ExecutionRouter.execute(
                engine=execution_engine,
                order=order,
                row=row
            )
    def cancel(self, order):

        order.cancel()

        print(
            f"Order Cancelled : {order.side}"
        )