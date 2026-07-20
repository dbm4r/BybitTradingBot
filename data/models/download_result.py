from dataclasses import dataclass

import pandas as pd


@dataclass(slots=True)
class DownloadResult:

    dataframe: pd.DataFrame

    filename: str

    rows: int