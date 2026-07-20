from data.engine.historical_engine import (
    HistoricalEngine,
)
from data.engine.historical_engine_builder import (
    HistoricalEngineBuilder,
)
from data.cache.memory_cache import (
    MemoryCache,
)
from data.storage.csv_storage import (
    CsvStorage,
)


class FakeExchange:
    pass


def test_builder_creates_engine():

    builder = HistoricalEngineBuilder(
        exchange=FakeExchange(),
    )

    engine = builder.build()

    assert isinstance(
        engine,
        HistoricalEngine,
    )


def test_builder_default_storage_and_cache():

    builder = HistoricalEngineBuilder(
        exchange=FakeExchange(),
    )

    engine = builder.build()

    assert isinstance(
        engine.cache,
        MemoryCache,
    )

    assert isinstance(
        engine.downloader.storage,
        CsvStorage,
    )


def test_builder_custom_configuration():

    from data.storage.storage_type import (
        StorageType,
    )

    from data.cache.cache_type import (
        CacheType,
    )

    builder = (
        HistoricalEngineBuilder(
            exchange=FakeExchange(),
        )
        .with_storage(
            StorageType.CSV,
        )
        .with_cache(
            CacheType.MEMORY,
            size=50,
        )
    )

    engine = builder.build()

    assert engine.cache.max_entries == 50

    assert isinstance(
        engine.downloader.storage,
        CsvStorage,
    )