from abc import ABC, abstractmethod

from scanner.analysis_result import AnalysisResult


class BaseRanker(ABC):

    @abstractmethod
    def rank(
        self,
        analyses: list[AnalysisResult],
    ) -> list[AnalysisResult]:
        pass