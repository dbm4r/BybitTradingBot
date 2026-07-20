from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class DownloadRequest:

    symbol: str

    interval: str

    start: datetime

    end: datetime