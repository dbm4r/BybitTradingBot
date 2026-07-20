from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class DatasetMetadata:

    exchange: str

    symbol: str

    interval: str

    rows: int

    first_timestamp: datetime

    last_timestamp: datetime

    last_sync: datetime

    checksum: str

    storage: str

    engine_version: str