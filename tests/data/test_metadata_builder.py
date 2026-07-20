from datetime import UTC
from datetime import datetime

import pandas as pd

from data.metadata.metadata_builder import (
    MetadataBuilder,
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


def test_build_metadata():

    dataframe = create_dataframe()

    metadata = MetadataBuilder.build(
        dataframe=dataframe,
        exchange="Bybit",
        symbol="BTCUSDT",
        interval="1",
        storage="csv",
        engine_version="1.9.0",
    )

    assert metadata.exchange == "Bybit"

    assert metadata.symbol == "BTCUSDT"

    assert metadata.interval == "1"

    assert metadata.rows == 2

    assert metadata.first_timestamp == dataframe.iloc[0][
        "timestamp"
    ]

    assert metadata.last_timestamp == dataframe.iloc[-1][
        "timestamp"
    ]

    assert metadata.storage == "csv"

    assert metadata.engine_version == "1.9.0"

    assert len(
        metadata.checksum,
    ) == 64