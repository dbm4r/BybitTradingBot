from dataclasses import dataclass

import pandas as pd


@dataclass(slots=True)
class PipelineResult:

    dataframe: pd.DataFrame

    rows: int