from indicators.indicator_pipeline import IndicatorPipeline
from models.candle import Candle
from models.candle_series import CandleSeries
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision
from market.regime_classifier import RegimeClassifier
from market.regime_filter import RegimeFilter

class TradingPipeline:

    def __init__(
        self,
        strategy: BaseStrategy,
        symbol: str,
        interval: str,
        max_candles: int = 5000,
    ):

        self.strategy = strategy

        self.series = CandleSeries(
            symbol=symbol,
            interval=interval,
            max_size=max_candles,
        )

        self.indicator_pipeline = IndicatorPipeline()
        self.regime_classifier = RegimeClassifier()

        self.regime_filter = RegimeFilter()

        self.indicator_pipeline.add_many(
            *strategy.indicators
        )

    def process_candle(
        self,
        candle: Candle,
    ) -> StrategyDecision:

        self.series.add(candle)

        indicator_results = (
            self.indicator_pipeline.calculate(
                self.series
            )
        )

        context = StrategyContext(
            candles=self.series,
            indicators=indicator_results,
        )

        decision = self.strategy.evaluate(
            context
        )

        regime = self.regime_classifier.classify(
            self.series
        )

        allowed = self.regime_filter.allows(
            decision=decision,
            regime=regime,
        )

        if not allowed:
            return decision

        return decision
    def load_history(
        self,
        candle_series: CandleSeries,
    ) -> None:

        if (
            candle_series.symbol
            != self.series.symbol
        ):
            raise ValueError(
                "Symbol mismatch."
            )

        if (
            candle_series.interval
            != self.series.interval
        ):
            raise ValueError(
                "Interval mismatch."
            )

        self.series = candle_series

        self.indicator_pipeline.calculate(
            self.series
        )
    @property
    def candle_series(self) -> CandleSeries:

        return self.series