from pathlib import Path

import pandas as pd

from data.storage.storage import Storage


class CsvStorage(Storage):

    def save(
        self,
        dataframe: pd.DataFrame,
        filename: str,
    ) -> None:

        path = Path(filename)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        dataframe.to_csv(
            path,
            index=False,
        )

    def load(
        self,
        filename: str,
    ) -> pd.DataFrame:

        return pd.read_csv(
            filename,
        )

    def exists(
        self,
        filename: str,
    ) -> bool:

        return Path(filename).exists()