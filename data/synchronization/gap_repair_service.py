from abc import ABC
from abc import abstractmethod

from data.synchronization.gap_repair_request import (
    GapRepairRequest,
)
from data.synchronization.gap_repair_result import (
    GapRepairResult,
)


class GapRepairService(ABC):

    @abstractmethod
    def repair(
        self,
        request: GapRepairRequest,
    ) -> GapRepairResult:
        pass