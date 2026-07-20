from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class Page:

    start: datetime

    end: datetime

    limit: int