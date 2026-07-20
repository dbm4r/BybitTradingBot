from datetime import UTC
from datetime import datetime

import pandas as pd

from data.downloader.parallel_download_request import (
    ParallelDownloadRequest,
)
from data.downloader.parallel_downloader import (
    ParallelDownloader,
)
from data.models.download_request import (
    DownloadRequest,
)
from data.models.download_result import (
    DownloadResult,
)


class FakeDownloader:

    def download(
        self,
        request: DownloadRequest,
    ) -> DownloadResult:

        dataframe = pd.DataFrame(
            {
                "timestamp": [
                    datetime(
                        2024,
                        1,
                        1,
                        tzinfo=UTC,
                    )
                ],
                "close": [
                    100.0,
                ],
            }
        )

        return DownloadResult(
            dataframe=dataframe,
            filename=f"{request.symbol}.csv",
            rows=len(dataframe),
        )


class FailingDownloader:

    def download(
        self,
        request: DownloadRequest,
    ):

        raise RuntimeError(
            "Download failed"
        )


def create_request():

    return DownloadRequest(
        symbol="BTCUSDT",
        interval="1",
        start=datetime(
            2024,
            1,
            1,
            tzinfo=UTC,
        ),
        end=datetime(
            2024,
            1,
            2,
            tzinfo=UTC,
        ),
    )


def test_parallel_download_success():

    downloader = ParallelDownloader(
        FakeDownloader(),
    )

    request = ParallelDownloadRequest(
        requests=[
            create_request(),
            create_request(),
            create_request(),
        ],
        max_workers=2,
    )

    result = downloader.download(
        request,
    )

    assert result.completed == 3

    assert result.failed == 0

    assert len(
        result.downloads,
    ) == 3


def test_parallel_download_failure():

    downloader = ParallelDownloader(
        FailingDownloader(),
    )

    request = ParallelDownloadRequest(
        requests=[
            create_request(),
            create_request(),
        ]
    )

    result = downloader.download(
        request,
    )

    assert result.completed == 0

    assert result.failed == 2

    assert len(
        result.downloads,
    ) == 0


def test_parallel_empty_request():

    downloader = ParallelDownloader(
        FakeDownloader(),
    )

    request = ParallelDownloadRequest(
        requests=[],
    )

    result = downloader.download(
        request,
    )

    assert result.completed == 0

    assert result.failed == 0

    assert result.downloads == []