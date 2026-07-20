from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class SynchronizationPlan:

    download_required: bool

    start: datetime | None

    end: datetime | None