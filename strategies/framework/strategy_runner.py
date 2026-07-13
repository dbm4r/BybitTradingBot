from indicators.indicator_pipeline import IndicatorPipeline
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision
from models.candle_series import CandleSeries


class StrategyRunner:

    def run(
        self,
        strategy: BaseStrategy,
        candles: CandleSeries,
    ) -> StrategyDecision:

        pipeline = IndicatorPipeline()

        pipeline.add_many(
            *strategy.indicators
        )

        indicator_results = pipeline.calculate(
            candles
        )

        context = StrategyContext(
            candles=candles,
            indicators=indicator_results,
        )

        return strategy.evaluate(
            context
        )