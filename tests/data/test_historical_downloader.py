import os

from datetime import UTC
from datetime import datetime

import pandas as pd

from data.downloader.historical_downloader import (
    HistoricalDownloader,
)

from data.metadata.json_metadata_service import (
    JsonMetadataService,
)

from data.models.download_request import (
    DownloadRequest,
)


from data.storage.csv_storage import (
    CsvStorage,
)

from data.synchronization.csv_synchronization_service import (
    CsvSynchronizationService,
)

from data.synchronization.dataframe_merge_service import (
    DataFrameMergeService,
)


class FakeProvider:

    def download(
        self,
        request,
    ):

        return {
            "result": {
                "list": [
                    [
                        "1704067260000",
                        "105",
                        "115",
                        "100",
                        "110",
                        "60",
                        "6000",
                    ],
                    [
                        "1704067200000",
                        "100",
                        "110",
                        "90",
                        "105",
                        "50",
                        "5000",
                    ],
                ]
            }
        }


def test_download(
    tmp_path,
):

    os.chdir(
        tmp_path,
    )

    storage = CsvStorage()

    metadata = JsonMetadataService()

    synchronization = CsvSynchronizationService(
        metadata_service=metadata,
    )

    downloader = HistoricalDownloader(
        provider=FakeProvider(),
        storage=storage,
        synchronization=synchronization,
        merge_service=DataFrameMergeService(),
        metadata_service=metadata,
    )

    request = DownloadRequest(
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

    result = downloader.download(
        request,
    )

    assert isinstance(
        result.dataframe,
        pd.DataFrame,
    )

    assert result.rows == 2

    assert storage.exists(
        result.filename,
    )

    assert metadata.exists(
        result.filename,
    )