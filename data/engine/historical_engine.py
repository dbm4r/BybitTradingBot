from data.cache.historical_cache import (
    HistoricalCache,
)

from data.downloader.historical_downloader import (
    HistoricalDownloader,
)

from data.models.download_request import (
    DownloadRequest,
)

from data.models.download_result import (
    DownloadResult,
)

from data.paths.historical_path_builder import (
    HistoricalPathBuilder,
)


class HistoricalEngine:

    def __init__(
        self,
        downloader: HistoricalDownloader,
        cache: HistoricalCache,
    ):

        self.downloader = downloader
        self.cache = cache

    def download(
        self,
        request: DownloadRequest,
    ) -> DownloadResult:

        filename = HistoricalPathBuilder.build(
            symbol=request.symbol,
            interval=request.interval,
        )

        dataframe = self.cache.get(
            filename,
        )

        if dataframe is not None:

            return DownloadResult(
                dataframe=dataframe,
                filename=filename,
                rows=len(dataframe),
            )

        result = self.downloader.download(
            request,
        )

        self.cache.put(
            key=result.filename,
            dataframe=result.dataframe,
        )

        return result

    def load(
        self,
        filename: str,
    ):

        return self.cache.get(
            filename,
        )

    def contains(
        self,
        filename: str,
    ) -> bool:

        return self.cache.contains(
            filename,
        )

    def clear_cache(
        self,
    ) -> None:

        self.cache.clear()