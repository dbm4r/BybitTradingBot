from datetime import datetime

from orders.limit_order import LimitOrder
from orders.order_status import OrderStatus


order = LimitOrder(
    symbol="BTCUSDT",
    side="BUY",
    quantity=2,
    limit_price=100,
    timestamp=datetime.now(),
)

assert order.limit_price == 100
assert order.remaining_quantity == 2
assert order.status == OrderStatus.PENDING

print("✓ LimitOrder tests passed")