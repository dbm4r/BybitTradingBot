from abc import ABC
from abc import abstractmethod

from data.metadata.dataset_metadata import (
    DatasetMetadata,
)


class MetadataService(ABC):

    @abstractmethod
    def save(
        self,
        metadata: DatasetMetadata,
        filename: str,
    ) -> None:
        pass

    @abstractmethod
    def load(
        self,
        filename: str,
    ) -> DatasetMetadata:
        pass

    @abstractmethod
    def exists(
        self,
        filename: str,
    ) -> bool:
        pass