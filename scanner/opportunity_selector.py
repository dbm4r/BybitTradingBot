from scanner.analysis_result import AnalysisResult


class OpportunitySelector:

    def select(
        self,
        analyses: list[AnalysisResult],
        limit: int,
    ) -> list[AnalysisResult]:

        return analyses[:limit]