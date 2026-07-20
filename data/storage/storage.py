from abc import ABC, abstractmethod

import pandas as pd


class Storage(ABC):

    @abstractmethod
    def save(
        self,
        dataframe: pd.DataFrame,
        filename: str,
    ) -> None:
        pass

    @abstractmethod
    def load(
        self,
        filename: str,
    ) -> pd.DataFrame:
        pass

    @abstractmethod
    def exists(
        self,
        filename: str,
    ) -> bool:
        pass