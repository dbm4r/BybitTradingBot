from indicators.indicator_pipeline import IndicatorPipeline
from models.candle import Candle
from models.candle_series import CandleSeries
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision
from market.regime_classifier import RegimeClassifier
from market.regime_filter import RegimeFilter
from market.multi_timeframe_context import MultiTimeframeContext
from market.timeframe import Timeframe
from market.timeframe_context import TimeframeContext
from market.timeframe_synchronizer import TimeframeSynchronizer
from market.higher_timeframe_confirmation import (
    HigherTimeframeConfirmation,
)
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
        self.multi_timeframe = MultiTimeframeContext(
            contexts={
                Timeframe.M5.value: TimeframeContext(
                    timeframe=Timeframe.M5.value,
                    candles=CandleSeries(
                        symbol=symbol,
                        interval=Timeframe.M5.value,
                    ),
                ),
                Timeframe.M15.value: TimeframeContext(
                    timeframe=Timeframe.M15.value,
                    candles=CandleSeries(
                        symbol=symbol,
                        interval=Timeframe.M15.value,
                    ),
                ),
                Timeframe.H1.value: TimeframeContext(
                    timeframe=Timeframe.H1.value,
                    candles=CandleSeries(
                        symbol=symbol,
                        interval=Timeframe.H1.value,
                    ),
                ),
                Timeframe.H4.value: TimeframeContext(
                    timeframe=Timeframe.H4.value,
                    candles=CandleSeries(
                        symbol=symbol,
                        interval=Timeframe.H4.value,
                    ),
                ),
                Timeframe.D1.value: TimeframeContext(
                    timeframe=Timeframe.D1.value,
                    candles=CandleSeries(
                        symbol=symbol,
                        interval=Timeframe.D1.value,
                    ),
                ),
            }
        )
        self.synchronizer = TimeframeSynchronizer(
            self.multi_timeframe,
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
        self.synchronizer.update(
            candle,
        )

        indicator_results = (
            self.indicator_pipeline.calculate(
                self.series
            )
        )

        context = StrategyContext(
            candles=self.series,
            indicators=indicator_results,
            timeframes=self.multi_timeframe,
        )

        decision = self.strategy.evaluate(
            context
        )

        regime = self.regime_classifier.classify(
            self.series
        )

        allowed, reason = self.regime_filter.allows(
            strategy=self.strategy,
            regime=regime,
        )

        if not allowed:
            return StrategyDecision.hold(
                candle=decision.candle,
                strategy=decision.strategy,
                reason=reason,
            )
        if not HigherTimeframeConfirmation.confirms(
            context=context,
            strategy=self.strategy,
        ):
            return StrategyDecision.hold(
                candle=decision.candle,
                strategy=decision.strategy,
                reason="Higher timeframe confirmation failed.",
            )

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