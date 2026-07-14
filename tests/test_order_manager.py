from datetime import datetime

from orders.market_order import MarketOrder
from orders.order_manager import OrderManager
from orders.order_status import OrderStatus


class DummyEventBus:

    def publish(self, event, order):
        pass


class DummyEngine:

    def __init__(self):
        self.events = DummyEventBus()


manager = OrderManager()

engine = DummyEngine()

order = MarketOrder(
    symbol="BTCUSDT",
    side="BUY",
    quantity=2,
    timestamp=datetime.now(),
)

manager.submit(
    engine,
    order,
)

assert len(manager.all_orders()) == 1

manager.fill(
    engine=engine,
    order=order,
    quantity=1,
    price=100,
    timestamp=datetime.now(),
)

assert order.status == OrderStatus.PARTIALLY_FILLED
assert order.remaining_quantity == 1
assert order.filled_quantity == 1

manager.fill(
    engine=engine,
    order=order,
    quantity=1,
    price=100,
    timestamp=datetime.now(),
)

assert order.status == OrderStatus.FILLED
assert order.remaining_quantity == 0
assert order.filled_quantity == 2

print("✓ OrderManager tests passed")