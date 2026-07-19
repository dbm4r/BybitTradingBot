from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ExchangeOrder:

    order_id: str
    symbol: str
    side: str
    quantity: float
    status: str

    average_price: float | None = None
    client_order_id: str | None = None
    filled_quantity: float = 0.0
    remaining_quantity: float = 0.0
    created_at: datetime | None = None
    updated_at: datetime | None = None
    raw_response: dict | None = None