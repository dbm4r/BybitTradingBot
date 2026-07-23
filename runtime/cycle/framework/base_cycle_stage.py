from abc import ABC
from abc import abstractmethod


class BaseCycleStage(ABC):

    @abstractmethod
    def execute(
        self,
        context,
    ):
        """
        Execute a single trading cycle stage.
        """