from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class SynchronizationState:

    exists: bool

    first_timestamp: datetime | None

    last_timestamp: datetime | None

    rows: int