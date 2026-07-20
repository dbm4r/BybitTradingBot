from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class HistoricalDataRequest:

    symbol: str

    interval: str

    start: datetime

    end: datetime

    limit: int