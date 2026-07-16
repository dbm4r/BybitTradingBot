from scanner.analysis_result import AnalysisResult
from scanner.filters.base_filter import BaseFilter


class FilterPipeline:

    def __init__(
        self,
        filters: list[BaseFilter],
    ):

        self.filters = filters

    def filter(
        self,
        analysis: AnalysisResult,
    ) -> bool:

        for filter_ in self.filters:

            if not filter_.filter(
                analysis
            ):
                return False

        return True