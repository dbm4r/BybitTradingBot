from datetime import UTC
from datetime import datetime

from data.metadata.dataset_metadata import (
    DatasetMetadata,
)
from data.metadata.json_metadata_service import (
    JsonMetadataService,
)


def create_metadata():

    return DatasetMetadata(
        exchange="Bybit",
        symbol="BTCUSDT",
        interval="1",
        rows=100,
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
        checksum="abc123",
        storage="csv",
        engine_version="1.9.0",
    )


def test_save_load_exists(tmp_path):

    service = JsonMetadataService()

    filename = str(
        tmp_path / "BTCUSDT.csv"
    )

    metadata = create_metadata()

    service.save(
        metadata,
        filename,
    )

    assert service.exists(
        filename,
    )

    loaded = service.load(
        filename,
    )

    assert loaded == metadata