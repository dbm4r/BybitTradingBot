from data.cache.cache_factory import (
    CacheFactory,
)
from data.cache.cache_type import (
    CacheType,
)

from data.downloader.historical_downloader import (
    HistoricalDownloader,
)

from data.engine.historical_engine import (
    HistoricalEngine,
)

from data.metadata.json_metadata_service import (
    JsonMetadataService,
)

from data.providers.bybit_historical_data_provider import (
    BybitHistoricalDataProvider,
)

from data.storage.storage_factory import (
    StorageFactory,
)
from data.storage.storage_type import (
    StorageType,
)

from data.synchronization.csv_synchronization_service import (
    CsvSynchronizationService,
)
from data.synchronization.dataframe_merge_service import (
    DataFrameMergeService,
)

from exchange.exchange import Exchange


class HistoricalEngineBuilder:

    def __init__(
        self,
        exchange: Exchange,
    ):

        self.exchange = exchange

        self.storage_type = StorageType.CSV
        self.cache_type = CacheType.MEMORY
        self.cache_size = 10

    def with_storage(
        self,
        storage: StorageType,
    ):

        self.storage_type = storage

        return self

    def with_cache(
        self,
        cache: CacheType,
        size: int = 10,
    ):

        self.cache_type = cache
        self.cache_size = size

        return self

    def build(
        self,
    ) -> HistoricalEngine:

        storage = StorageFactory.create(
            self.storage_type,
        )

        cache = CacheFactory.create(
            self.cache_type,
            self.cache_size,
        )

        metadata = JsonMetadataService()

        synchronization = (
            CsvSynchronizationService(
                metadata_service=metadata,
            )
        )

        provider = (
            BybitHistoricalDataProvider(
                exchange=self.exchange,
            )
        )

        downloader = HistoricalDownloader(
            provider=provider,
            storage=storage,
            synchronization=synchronization,
            merge_service=DataFrameMergeService(),
            metadata_service=metadata,
        )

        return HistoricalEngine(
            downloader=downloader,
            cache=cache,
        )