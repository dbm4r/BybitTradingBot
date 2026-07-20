from abc import ABC
from abc import abstractmethod

from data.synchronization.synchronization_state import (
    SynchronizationState,
)


class SynchronizationService(ABC):

    @abstractmethod
    def inspect(
        self,
        filename: str,
    ) -> SynchronizationState:
        pass