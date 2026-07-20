from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class MissingRange:

    start: datetime

    end: datetime

    missing_candles: int