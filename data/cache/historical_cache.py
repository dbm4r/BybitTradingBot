from abc import ABC
from abc import abstractmethod

import pandas as pd


class HistoricalCache(ABC):

    @abstractmethod
    def get(
        self,
        key: str,
    ) -> pd.DataFrame | None:
        pass

    @abstractmethod
    def put(
        self,
        key: str,
        dataframe: pd.DataFrame,
    ) -> None:
        pass

    @abstractmethod
    def contains(
        self,
        key: str,
    ) -> bool:
        pass

    @abstractmethod
    def clear(
        self,
    ) -> None:
        pass