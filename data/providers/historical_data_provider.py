from abc import ABC
from abc import abstractmethod

from data.models.historical_data_request import (
    HistoricalDataRequest,
)


class HistoricalDataProvider(ABC):

    @abstractmethod
    def download(
        self,
        request: HistoricalDataRequest,
    ):
        pass