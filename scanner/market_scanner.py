from scanner.symbol_analyzer import SymbolAnalyzer
from scanner.universe import SymbolUniverse
from scanner.ranking.score_ranker import ScoreRanker


class MarketScanner:

    def __init__(
        self,
        universe: SymbolUniverse,
        analyzer: SymbolAnalyzer,
    ):

        self.universe = universe
        self.analyzer = analyzer
        self.ranker = ScoreRanker()

    def scan( 
        self,
    ):

        analyses = []

        for symbol in self.universe:

            analyses.append(
                self.analyzer.analyze(
                    symbol
                )
            )

        return self.ranker.rank(
            analyses
        )