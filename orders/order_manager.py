from orders.order_status import OrderStatus


class OrderManager:

    def __init__(self):

        self.orders = []

    def submit(self, order):

        self.orders.append(order)

        print(f"Order Submitted : {order.side}")

        return order

    def fill(
        self,
        order,
        price,
        timestamp
    ):

        order.status = OrderStatus.FILLED
        order.filled_price = price
        order.filled_time = timestamp

        print(
            f"Order Filled : "
            f"{order.side} @ {price:.2f}"
        )

        return order
    def all_orders(self):

        return self.orders