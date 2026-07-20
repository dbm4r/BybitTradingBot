from collections import OrderedDict
from datetime import UTC
from datetime import datetime
import pandas as pd

from data.cache.cache_entry import CacheEntry
from data.cache.historical_cache import HistoricalCache


class MemoryCache(
    HistoricalCache,
):

    def __init__(
        self,
        max_entries: int = 10,
    ):

        self.max_entries = max_entries
        self.entries: OrderedDict[
            str,
            CacheEntry,
        ] = OrderedDict()

    def get(
        self,
        key: str,
    ) -> pd.DataFrame | None:

        entry = self.entries.get(
            key,
        )

        if entry is None:

            return None

        entry.last_access = datetime.now(
            UTC,
        )

        self.entries.move_to_end(
            key,
        )

        return entry.dataframe

    def put(
        self,
        key: str,
        dataframe: pd.DataFrame,
    ) -> None:

        now = datetime.now(
            UTC,
        )

        if key in self.entries:

            self.entries[key] = CacheEntry(
                key=key,
                dataframe=dataframe,
                created_at=self.entries[
                    key
                ].created_at,
                last_access=now,
            )

            self.entries.move_to_end(
                key,
            )

            return

        if (
            len(self.entries)
            >= self.max_entries
        ):

            self.entries.popitem(
                last=False,
            )

        self.entries[key] = CacheEntry(
            key=key,
            dataframe=dataframe,
            created_at=now,
            last_access=now,
        )

    def contains(
        self,
        key: str,
    ) -> bool:

        return key in self.entries

    def clear(
        self,
    ) -> None:

        self.entries.clear()

    def remove(
        self,
        key: str,
    ) -> None:

        self.entries.pop(
            key,
            None,
        )

    def size(
        self,
    ) -> int:

        return len(
            self.entries,
        )

    def keys(
        self,
    ) -> list[str]:

        return list(
            self.entries.keys(),
        )