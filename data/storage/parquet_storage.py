from pathlib import Path

import pandas as pd

from data.storage.storage import Storage


class ParquetStorage(
    Storage,
):

    def save(
        self,
        dataframe: pd.DataFrame,
        filename: str,
    ) -> None:

        path = Path(
            filename,
        ).with_suffix(
            ".parquet"
        )

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        dataframe.to_parquet(
            path,
            index=False,
        )

    def load(
        self,
        filename: str,
    ) -> pd.DataFrame:

        path = Path(
            filename,
        ).with_suffix(
            ".parquet"
        )

        return pd.read_parquet(
            path,
        )

    def exists(
        self,
        filename: str,
    ) -> bool:

        return Path(
            filename,
        ).with_suffix(
            ".parquet"
        ).exists()

    def delete(
        self,
        filename: str,
    ) -> None:

        path = Path(
            filename,
        ).with_suffix(
            ".parquet"
        )

        if path.exists():

            path.unlink()