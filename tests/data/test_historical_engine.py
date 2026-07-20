from datetime import UTC
from datetime import datetime

import pandas as pd

from data.engine.historical_engine import (
    HistoricalEngine,
)

from data.models.download_request import (
    DownloadRequest,
)

from data.models.download_result import (
    DownloadResult,
)


class FakeDownloader:

    def __init__(self):

        self.calls = 0

    def download(
        self,
        request,
    ):

        self.calls += 1

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
                    100,
                ],
            }
        )

        return DownloadResult(
            dataframe=dataframe,
            filename="BTCUSDT.csv",
            rows=1,
        )


class FakeCache:

    def __init__(self):

        self.data = {}

    def get(
        self,
        key,
    ):

        return self.data.get(
            key,
        )

    def put(
        self,
        key,
        dataframe,
    ):

        self.data[key] = dataframe

    def contains(
        self,
        key,
    ):

        return key in self.data

    def clear(
        self,
    ):

        self.data.clear()


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


def test_download_cache_miss():

    downloader = FakeDownloader()

    cache = FakeCache()

    engine = HistoricalEngine(
        downloader=downloader,
        cache=cache,
    )

    result = engine.download(
        create_request(),
    )

    assert result.rows == 1

    assert downloader.calls == 1

    assert cache.contains(
        "BTCUSDT.csv",
    )


def test_download_cache_hit():

    downloader = FakeDownloader()

    cache = FakeCache()

    dataframe = pd.DataFrame(
        {
            "close": [
                200,
            ]
        }
    )

    cache.put(
        "BTCUSDT.csv",
        dataframe,
    )

    engine = HistoricalEngine(
        downloader=downloader,
        cache=cache,
    )

    result = engine.load(
        "BTCUSDT.csv",
    )

    assert result.equals(
        dataframe,
    )

    assert downloader.calls == 0


def test_clear_cache():

    cache = FakeCache()

    engine = HistoricalEngine(
        downloader=FakeDownloader(),
        cache=cache,
    )

    cache.put(
        "BTCUSDT.csv",
        pd.DataFrame(),
    )

    engine.clear_cache()

    assert len(
        cache.data,
    ) == 0