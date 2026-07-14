from orders.order_status import OrderStatus
from execution.execution_router import ExecutionRouter
from orders.oco_manager import OCOManager
from events.event_names import EventNames
from models.candle import Candle
class OrderManager:

    def __init__(self):
        self.oco_manager = OCOManager()

        self.orders = []

    def submit(self, engine, order):
        engine.events.publish(
            EventNames.ORDER_SUBMITTED,
            order
        )

        self.orders.append(order)


        return order

    def fill(
        self,
        engine,
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
            engine.events.publish(
                EventNames.ORDER_FILLED,
                order
            )

        else:

            order.status = OrderStatus.PARTIALLY_FILLED


        return order
    def all_orders(self):

        return self.orders
    def submit_pending(
        self,
        engine,
        order
    ):

        engine.events.publish(
            EventNames.ORDER_SUBMITTED,
            order
        )

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
        engine,
        candle: Candle,
    ) -> None:

        for order in self.pending():

            if (
                order.expires_at is not None
                and candle.timestamp >= order.expires_at
            ):
                order.expire()
                continue

            if not order.should_fill(candle):
                continue

            self.fill(
                engine=engine,
                order=order,
                quantity=order.remaining_quantity,
                price=order.execution_price,
                timestamp=candle.timestamp,
            )

            ExecutionRouter.execute(
                engine=engine,
                order=order,
                candle=candle,
            )
    def cancel(self, order):

        order.cancel()

        print(
            f"Order Cancelled : {order.side}"
        )
    def restore(
        self,
        order
    ):

        self.orders.append(order)
    def clear(self):

        self.orders.clear()