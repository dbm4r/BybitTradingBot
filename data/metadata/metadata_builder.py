from datetime import UTC
from datetime import datetime
import hashlib

import pandas as pd

from data.metadata.dataset_metadata import (
    DatasetMetadata,
)


class MetadataBuilder:

    @staticmethod
    def build(
        dataframe: pd.DataFrame,
        exchange: str,
        symbol: str,
        interval: str,
        storage: str,
        engine_version: str,
    ) -> DatasetMetadata:

        if dataframe.empty:

            raise ValueError(
                "Cannot build metadata for an empty dataframe."
            )

        checksum = hashlib.sha256(
            dataframe.to_csv(
                index=False,
            ).encode(
                "utf-8"
            )
        ).hexdigest()

        return DatasetMetadata(
            exchange=exchange,
            symbol=symbol,
            interval=interval,
            rows=len(
                dataframe,
            ),
            first_timestamp=dataframe.iloc[0][
                "timestamp"
            ],
            last_timestamp=dataframe.iloc[-1][
                "timestamp"
            ],
            last_sync=datetime.now(
                UTC,
            ),
            checksum=checksum,
            storage=storage,
            engine_version=engine_version,
        )