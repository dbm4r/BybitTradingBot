from datetime import datetime

from orders.stop_limit_order import StopLimitOrder
from orders.order_status import OrderStatus


order = StopLimitOrder(
    symbol="BTCUSDT",
    side="BUY",
    quantity=1,
    stop_price=100,
    limit_price=99,
    timestamp=datetime.now(),
)

assert order.stop_price == 100
assert order.limit_price == 99
assert order.status == OrderStatus.PENDING

print("✓ StopLimitOrder tests passed")