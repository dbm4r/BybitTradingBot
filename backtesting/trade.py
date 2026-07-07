from dataclasses import dataclass
from datetime import datetime


@dataclass
class Trade:
    """
    Represents one completed trade.

    Stores all information about a position from
    entry until exit.
    """

    symbol: str

    strategy: str

    entry_time: datetime
    exit_time: datetime

    entry_price: float
    exit_price: float

    quantity: float

    gross_profit: float

    fees: float

    net_profit: float

    profit_percent: float

    duration: float
    exit_reason: str