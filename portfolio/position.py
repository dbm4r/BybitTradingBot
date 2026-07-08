from dataclasses import dataclass
from datetime import datetime


@dataclass
class Position:

    symbol: str

    quantity: float = 0

    entry_price: float | None = None

    entry_time: datetime | None = None

    stop_price: float | None = None

    take_profit_price: float | None = None

    highest_price: float | None = None

    break_even_active: bool = False
    trailing_active: bool = False