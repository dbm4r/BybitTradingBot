from dataclasses import dataclass

from datetime import datetime


@dataclass(
    slots=True,
)
class OrderResult:

    success: bool

    order_id: str | None

    quantity: float

    price: float

    fee: float

    timestamp: datetime

    error: str | None = None