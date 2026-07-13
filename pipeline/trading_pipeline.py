from indicators.indicator_pipeline import IndicatorPipeline
from models.candle import Candle
from models.candle_series import CandleSeries
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision


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

        return self.strategy.evaluate(
            context
        )

    @property
    def candle_series(self) -> CandleSeries:

        return self.series