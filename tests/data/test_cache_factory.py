import pytest

from data.cache.cache_factory import CacheFactory
from data.cache.cache_type import CacheType
from data.cache.memory_cache import MemoryCache


def test_create_memory_cache():

    cache = CacheFactory.create(
        CacheType.MEMORY,
    )

    assert isinstance(
        cache,
        MemoryCache,
    )


def test_memory_cache_size():

    cache = CacheFactory.create(
        CacheType.MEMORY,
        max_entries=25,
    )

    assert cache.max_entries == 25


def test_invalid_cache():

    with pytest.raises(
        ValueError,
    ):

        CacheFactory.create(
            "invalid",
        )