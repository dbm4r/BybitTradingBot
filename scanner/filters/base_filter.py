from abc import ABC, abstractmethod

from scanner.analysis_result import AnalysisResult


class BaseFilter(ABC):

    @abstractmethod
    def filter(
        self,
        analysis: AnalysisResult,
    ) -> bool:
        pass