from dataclasses import dataclass
from datetime import datetime

import pandas as pd


@dataclass(slots=True)
class CacheEntry:

    key: str

    dataframe: pd.DataFrame

    created_at: datetime

    last_access: datetime