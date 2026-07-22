from dataclasses import dataclass

from datetime import datetime


@dataclass(
    slots=True,
)
class OrderRequest:

    symbol: str

    side: str

    quantity: float

    price: float

    timestamp: datetime

    order_type: str = "MARKET"