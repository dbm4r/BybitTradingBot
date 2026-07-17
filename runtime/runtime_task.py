from abc import ABC, abstractmethod


class RuntimeTask(ABC):

    @abstractmethod
    def run(
        self,
    ) -> None:
        pass