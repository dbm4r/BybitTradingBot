from datetime import UTC
from datetime import datetime

import pandas as pd


from data.validation.dataset_validator import (
    DatasetValidator,
)


def create_dataframe():

    return pd.DataFrame(
        {
            "timestamp": [
                datetime(
                    2024,
                    1,
                    1,
                    tzinfo=UTC,
                ),
                datetime(
                    2024,
                    1,
                    2,
                    tzinfo=UTC,
                ),
            ],
            "close": [
                100,
                110,
            ],
        }
    )


def create_metadata(
    dataframe,
):

    from data.metadata.metadata_builder import (
        MetadataBuilder,
    )

    return MetadataBuilder.build(
        dataframe=dataframe,
        exchange="Bybit",
        symbol="BTCUSDT",
        interval="1",
        storage="csv",
        engine_version="1.9.0",
    )


def test_valid_dataset():

    dataframe = create_dataframe()

    metadata = create_metadata(
        dataframe,
    )

    result = DatasetValidator.validate(
        dataframe,
        metadata,
    )

    assert result.valid is True


def test_row_count_mismatch():

    dataframe = create_dataframe()

    metadata = create_metadata(
        dataframe,
    )

    modified = dataframe.iloc[:1]

    result = DatasetValidator.validate(
        modified,
        metadata,
    )

    assert result.valid is False

    assert result.message == (
        "Row count mismatch"
    )


def test_checksum_mismatch():

    dataframe = create_dataframe()

    metadata = create_metadata(
        dataframe,
    )

    modified = dataframe.copy()

    modified.loc[0, "close"] = 999

    result = DatasetValidator.validate(
        modified,
        metadata,
    )

    assert result.valid is False

    assert result.message == (
        "Checksum mismatch"
    )