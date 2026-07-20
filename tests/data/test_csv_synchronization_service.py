from datetime import UTC
from datetime import datetime

from data.metadata.dataset_metadata import (
    DatasetMetadata,
)
from data.metadata.json_metadata_service import (
    JsonMetadataService,
)
from data.synchronization.csv_synchronization_service import (
    CsvSynchronizationService,
)


def create_metadata():

    return DatasetMetadata(
        exchange="Bybit",
        symbol="BTCUSDT",
        interval="1",
        rows=500,
        first_timestamp=datetime(
            2024,
            1,
            1,
            tzinfo=UTC,
        ),
        last_timestamp=datetime(
            2024,
            1,
            2,
            tzinfo=UTC,
        ),
        last_sync=datetime(
            2024,
            1,
            2,
            tzinfo=UTC,
        ),
        checksum="abc",
        storage="csv",
        engine_version="1.9.0",
    )


def test_missing_dataset(tmp_path):

    filename = str(
        tmp_path / "BTCUSDT.csv"
    )

    service = CsvSynchronizationService(
        metadata_service=JsonMetadataService(),
    )

    state = service.inspect(
        filename,
    )

    assert state.exists is False
    assert state.rows == 0
    assert state.first_timestamp is None
    assert state.last_timestamp is None


def test_existing_dataset(tmp_path):

    filename = str(
        tmp_path / "BTCUSDT.csv"
    )

    metadata_service = JsonMetadataService()

    metadata_service.save(
        create_metadata(),
        filename,
    )

    service = CsvSynchronizationService(
        metadata_service=metadata_service,
    )

    state = service.inspect(
        filename,
    )

    assert state.exists is True
    assert state.rows == 500

    assert state.first_timestamp == datetime(
        2024,
        1,
        1,
        tzinfo=UTC,
    )

    assert state.last_timestamp == datetime(
        2024,
        1,
        2,
        tzinfo=UTC,
    )