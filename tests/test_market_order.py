from datetime import datetime

from orders.market_order import MarketOrder
from orders.order_status import OrderStatus


order = MarketOrder(
    symbol="BTCUSDT",
    side="BUY",
    quantity=1.5,
    timestamp=datetime.now(),
)

assert order.symbol == "BTCUSDT"
assert order.side == "BUY"
assert order.quantity == 1.5

assert order.remaining_quantity == 1.5
assert order.filled_quantity == 0

assert order.status == OrderStatus.PENDING

print("✓ MarketOrder tests passed")