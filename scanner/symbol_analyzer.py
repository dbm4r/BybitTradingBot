from market.market_data_provider import MarketDataProvider
from exchange.exchange_symbol import ExchangeSymbol
from scanner.context_builder import ContextBuilder
from scanner.candle_loader import CandleLoader
from scanner.market_analyzer import MarketAnalyzer
from scanner.market_analysis import MarketAnalysis
from scanner.analysis_result import AnalysisResult
from scanner.scoring.overall_scorer import OverallScorer


class SymbolAnalyzer:

    def __init__(
        self,
        provider: MarketDataProvider,
    ):

        self.provider = provider
        self.scorer = OverallScorer()
        self.market_analyzer = MarketAnalyzer()

    def load_candles(
        self,
        symbol: ExchangeSymbol,
        interval: str,
        limit: int = 200,
    ):

        response = self.provider.get_candles(
            symbol=symbol.symbol,
            interval=interval,
            limit=limit,
        )

        return CandleLoader.load(
            response=response,
            symbol=symbol.symbol,
            interval=interval,
        )

    def build_context(
        self,
        symbol: ExchangeSymbol,
        interval: str,
        limit: int = 200,
    ):

        candles = self.load_candles(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        return ContextBuilder.build(
            candles
        )

    def analyze_market(
        self,
        symbol: ExchangeSymbol,
        interval: str,
        limit: int = 200,
    ) -> MarketAnalysis:

        candles = self.load_candles(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        context = self.build_context(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        return self.market_analyzer.analyze(
            context=context,
            candles=candles,
        )

    def analyze(
        self,
        symbol: ExchangeSymbol,
        interval: str = "1",
        limit: int = 200,
    ) -> AnalysisResult:

        market = self.analyze_market(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        score = self.scorer.score(
            market
        )

        return AnalysisResult(
            symbol=symbol,
            regime=market.regime,
            score=score,
            passed=True,
            reason=None,
        )