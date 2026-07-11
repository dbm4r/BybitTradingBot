from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExchangeTrade:

    trade_id: str

    order_id: str

    symbol: str

    side: str

    quantity: float

    price: float

    fee: float

    timestamp: datetime

    def __str__(self):

        return (
            f"{self.symbol} | "
            f"{self.side} | "
            f"{self.quantity:.6f} @ "
            f"{self.price:.2f}"
        )