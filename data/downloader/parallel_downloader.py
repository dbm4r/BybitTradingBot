from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from data.downloader.historical_downloader import (
    HistoricalDownloader,
)
from data.downloader.parallel_download_request import (
    ParallelDownloadRequest,
)
from data.downloader.parallel_download_result import (
    ParallelDownloadResult,
)


class ParallelDownloader:

    def __init__(
        self,
        downloader: HistoricalDownloader,
    ):

        self.downloader = downloader

    def download(
        self,
        request: ParallelDownloadRequest,
    ) -> ParallelDownloadResult:

        downloads = []
        failed = 0

        with ThreadPoolExecutor(
            max_workers=request.max_workers,
        ) as executor:

            futures = [
                executor.submit(
                    self.downloader.download,
                    download_request,
                )
                for download_request in request.requests
            ]

            for future in as_completed(
                futures,
            ):

                try:

                    downloads.append(
                        future.result()
                    )

                except Exception:

                    failed += 1

        return ParallelDownloadResult(
            downloads=downloads,
            completed=len(downloads),
            failed=failed,
        )