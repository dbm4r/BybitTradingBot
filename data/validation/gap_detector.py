from abc import ABC
from abc import abstractmethod

import pandas as pd

from data.validation.gap_report import (
    GapReport,
)


class GapDetector(ABC):

    @abstractmethod
    def detect(
        self,
        dataframe: pd.DataFrame,
        interval: str,
    ) -> GapReport:
        pass