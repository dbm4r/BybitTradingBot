from abc import ABC
from abc import abstractmethod

import pandas as pd


class MergeService(ABC):

    @abstractmethod
    def merge(
        self,
        existing: pd.DataFrame,
        incoming: pd.DataFrame,
    ) -> pd.DataFrame:
        pass