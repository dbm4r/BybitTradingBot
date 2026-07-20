from data.downloader.download_job import DownloadJob
from data.downloader.paginator import Paginator

from data.metadata.metadata_builder import (
    MetadataBuilder,
)
from data.metadata.metadata_service import (
    MetadataService,
)
from data.storage.csv_storage import (
    CsvStorage,
)
from data.mappers.candle_dataframe_mapper import (
    CandleDataFrameMapper,
)
from data.models.download_request import (
    DownloadRequest,
)
from data.models.download_result import (
    DownloadResult,
)
from data.models.historical_data_request import (
    HistoricalDataRequest,
)

from data.paths.historical_path_builder import (
    HistoricalPathBuilder,
)

from data.pipeline.historical_pipeline import (
    HistoricalPipeline,
)

from data.providers.historical_data_provider import (
    HistoricalDataProvider,
)

from data.storage.storage import (
    Storage,
)

from data.synchronization.merge_service import (
    MergeService,
)

from data.synchronization.synchronization_planner import (
    SynchronizationPlanner,
)

from data.synchronization.synchronization_service import (
    SynchronizationService,
)

class HistoricalDownloader:

    def __init__(
        self,
        provider: HistoricalDataProvider,
        storage: Storage,
        synchronization: SynchronizationService,
        merge_service: MergeService,
        metadata_service: MetadataService,
        exchange: str = "Bybit",
        storage_format: str = "csv",
        engine_version: str = "1.9",
    ):

        self.provider = provider
        self.storage = storage
        self.synchronization = synchronization
        self.merge_service = merge_service
        self.metadata_service = metadata_service

        self.exchange = exchange
        self.storage_format = storage_format
        self.engine_version = engine_version
    def download(
        self,
        request: DownloadRequest,
    ) -> DownloadResult:

        filename = HistoricalPathBuilder.build(
            symbol=request.symbol,
            interval=request.interval,
        )

        state = self.synchronization.inspect(
            filename,
        )

        plan = SynchronizationPlanner.plan(
            request=request,
            state=state,
        )


        if not plan.download_required:

            dataframe = self.storage.load(
                filename,
            )

            return DownloadResult(
                dataframe=dataframe,
                filename=filename,
                rows=len(dataframe),
            )


        job = DownloadJob(
            symbol=request.symbol,
            interval=request.interval,
            start=plan.start,
            end=plan.end,
        )


        pipeline_results = []

        paginator = Paginator(
            job,
        )


        for page in paginator:

            response = self.provider.download(
                HistoricalDataRequest(
                    symbol=job.symbol,
                    interval=job.interval,
                    start=page.start,
                    end=page.end,
                    limit=page.limit,
                )
            )

            dataframe = HistoricalPipeline.process(
                response=response,
                symbol=job.symbol,
                interval=job.interval,
            )

            pipeline_results.append(
                dataframe,
            )


        if not pipeline_results:

            raise ValueError(
                "No historical data returned"
            )


        dataframe = pipeline_results[0]


        for incoming in pipeline_results[1:]:

            dataframe = self.merge_service.merge(
                existing=dataframe,
                incoming=incoming,
            )


        if state.exists:

            existing = self.storage.load(
                filename,
            )

            dataframe = self.merge_service.merge(
                existing=existing,
                incoming=dataframe,
            )


        self.storage.save(
            dataframe=dataframe,
            filename=filename,
        )


        metadata = MetadataBuilder.build(
            dataframe=dataframe,
            exchange=self.exchange,
            symbol=request.symbol,
            interval=request.interval,
            storage=self.storage_format,
            engine_version=self.engine_version,
        )


        self.metadata_service.save(
            metadata=metadata,
            filename=filename,
        )


        return DownloadResult(
            dataframe=dataframe,
            filename=filename,
            rows=len(dataframe),
        )
    

    @staticmethod
    def from_candles(
        candles,
    ):
        """
        Legacy compatibility wrapper.

        Converts a list of Candle objects into a DataFrame.
        """

        return CandleDataFrameMapper.map(
            candles,
        )

    @staticmethod
    def save_to_csv(
        dataframe,
        filename: str,
    ) -> None:
        """
        Legacy compatibility wrapper.
        """

        CsvStorage().save(
            dataframe=dataframe,
            filename=filename,
        )