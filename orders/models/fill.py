from dataclasses import dataclass
from datetime import datetime


@dataclass(
    frozen=True,
    slots=True,
)
class Fill:

    quantity: float

    price: float

    timestamp: datetime

    fee: float = 0.0