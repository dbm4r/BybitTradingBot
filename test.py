from datetime import datetime

from orders.stop_limit_order import StopLimitOrder

order = StopLimitOrder(
    symbol="BTCUSDT",
    side="BUY",
    quantity=1,
    stop_price=60500,
    limit_price=60520,
    timestamp=datetime.now()
)

print(order.triggered)

print(order.should_fill({
    "high": 60400,
    "low": 60300
}))

print(order.triggered)

print(order.should_fill({
    "high": 60550,
    "low": 60510
}))

print(order.triggered)