from scanner.analysis_result import AnalysisResult
from scanner.ranking.base_ranker import BaseRanker


class ScoreRanker(BaseRanker):

    def rank(
        self,
        analyses: list[AnalysisResult],
    ) -> list[AnalysisResult]:

        return sorted(
            analyses,
            key=lambda analysis: analysis.score,
            reverse=True,
        )