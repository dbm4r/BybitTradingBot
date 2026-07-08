from abc import ABC, abstractmethod

import pandas as pd


class BaseIndicator(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def parameters(self) -> dict:
        pass

    @abstractmethod
    def calculate(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        pass