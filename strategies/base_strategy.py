from abc import ABC, abstractmethod
import pandas as pd


class BaseStrategy(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def parameters(self) -> dict:
        pass

    @abstractmethod
    def generate_signals(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        pass