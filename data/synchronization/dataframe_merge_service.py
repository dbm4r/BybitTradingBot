import pandas as pd

from data.synchronization.merge_service import (
    MergeService,
)


class DataFrameMergeService(
    MergeService,
):

    def merge(
        self,
        existing: pd.DataFrame,
        incoming: pd.DataFrame,
    ) -> pd.DataFrame:

        dataframe = pd.concat(
            [
                existing,
                incoming,
            ],
            ignore_index=True,
        )

        dataframe = dataframe.drop_duplicates(
            subset="timestamp",
            keep="last",
        )

        dataframe = dataframe.sort_values(
            by="timestamp",
        )

        dataframe = dataframe.reset_index(
            drop=True,
        )

        return dataframe