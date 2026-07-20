from data.cache.cache_type import (
    CacheType,
)
from data.cache.historical_cache import (
    HistoricalCache,
)
from data.cache.memory_cache import (
    MemoryCache,
)


class CacheFactory:

    @staticmethod
    def create(
        cache_type: (
            CacheType | str
        ) = CacheType.MEMORY,
        max_entries: int = 10,
    ) -> HistoricalCache:

        if isinstance(
            cache_type,
            str,
        ):

            cache_type = CacheType(
                cache_type.lower()
            )

        match cache_type:

            case CacheType.MEMORY:

                return MemoryCache(
                    max_entries=max_entries,
                )

        raise ValueError(
            f"Unsupported cache type: "
            f"{cache_type}"
        )