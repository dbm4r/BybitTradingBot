from datetime import datetime

from orders.stop_order import StopOrder
from orders.order_status import OrderStatus


order = StopOrder(
    symbol="BTCUSDT",
    side="SELL",
    quantity=1,
    stop_price=90,
    timestamp=datetime.now(),
)

assert order.stop_price == 90
assert order.status == OrderStatus.PENDING

print("✓ StopOrder tests passed")