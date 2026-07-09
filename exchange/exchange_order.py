from dataclasses import dataclass


@dataclass
class ExchangeOrder:

    order_id: str

    symbol: str

    side: str

    quantity: float

    status: str

    average_price: float | None = None