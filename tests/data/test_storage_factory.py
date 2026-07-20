from data.storage.csv_storage import CsvStorage
from data.storage.parquet_storage import ParquetStorage
from data.storage.storage_factory import StorageFactory
from data.storage.storage_type import StorageType

import pytest


def test_create_csv_storage():

    storage = StorageFactory.create(
        StorageType.CSV,
    )

    assert isinstance(
        storage,
        CsvStorage,
    )


def test_create_parquet_storage():

    storage = StorageFactory.create(
        StorageType.PARQUET,
    )

    assert isinstance(
        storage,
        ParquetStorage,
    )


def test_invalid_storage():

    with pytest.raises(
        ValueError,
    ):

        StorageFactory.create(
            "invalid",
        )