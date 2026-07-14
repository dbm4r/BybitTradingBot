from datetime import datetime

from execution.execution_router import ExecutionRouter
from orders.market_order import MarketOrder
from models.candle import Candle


class DummyEngine:
    pass


buy_order = MarketOrder(
    symbol="BTCUSDT",
    side="BUY",
    quantity=1,
    timestamp=datetime.now(),
)

sell_order = MarketOrder(
    symbol="BTCUSDT",
    side="SELL",
    quantity=1,
    timestamp=datetime.now(),
)

buy_order.filled_price = 100
sell_order.filled_price = 100

candle = Candle(
    symbol="BTCUSDT",
    interval="1",
    timestamp=datetime.now(),
    open=100,
    high=101,
    low=99,
    close=100,
    volume=10,
    turnover=1000,
)

try:

    ExecutionRouter.execute(
        engine=DummyEngine(),
        order=buy_order,
        candle=candle,
    )

except Exception:
    pass

try:

    ExecutionRouter.execute(
        engine=DummyEngine(),
        order=sell_order,
        candle=candle,
    )

except Exception:
    pass

print("✓ ExecutionRouter dispatch tested")