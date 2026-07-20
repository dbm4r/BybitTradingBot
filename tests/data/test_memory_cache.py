from datetime import datetime

import pandas as pd

from data.cache.memory_cache import MemoryCache


def create_dataframe():

    return pd.DataFrame(
        {
            "timestamp": [
                datetime(2024, 1, 1),
            ],
            "close": [
                100.0,
            ],
        }
    )


def test_put_and_get():

    cache = MemoryCache()

    dataframe = create_dataframe()

    cache.put(
        "BTCUSDT",
        dataframe,
    )

    assert cache.contains(
        "BTCUSDT",
    )

    assert cache.get(
        "BTCUSDT",
    ).equals(
        dataframe,
    )


def test_cache_clear():

    cache = MemoryCache()

    cache.put(
        "BTCUSDT",
        create_dataframe(),
    )

    cache.clear()

    assert cache.size() == 0


def test_cache_remove():

    cache = MemoryCache()

    cache.put(
        "BTCUSDT",
        create_dataframe(),
    )

    cache.remove(
        "BTCUSDT",
    )

    assert not cache.contains(
        "BTCUSDT",
    )


def test_cache_keys():

    cache = MemoryCache()

    cache.put(
        "BTCUSDT",
        create_dataframe(),
    )

    cache.put(
        "ETHUSDT",
        create_dataframe(),
    )

    assert cache.keys() == [
        "BTCUSDT",
        "ETHUSDT",
    ]


def test_lru_eviction():

    cache = MemoryCache(
        max_entries=2,
    )

    cache.put(
        "BTC",
        create_dataframe(),
    )

    cache.put(
        "ETH",
        create_dataframe(),
    )

    cache.get(
        "BTC",
    )

    cache.put(
        "SOL",
        create_dataframe(),
    )

    assert cache.contains(
        "BTC",
    )

    assert cache.contains(
        "SOL",
    )

    assert not cache.contains(
        "ETH",
    )