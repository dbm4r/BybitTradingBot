from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class DownloadJob:

    symbol: str

    interval: str

    start: datetime

    end: datetime

    page_size: int = 1000