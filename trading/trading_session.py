from execution.decision_processor import (
    DecisionProcessor,
)
from models.candle import Candle
from pipeline.trading_pipeline import TradingPipeline
from strategies.framework.strategy_decision import (
    StrategyDecision,
)


class TradingSession:

    def __init__(
        self,
        engine,
        pipeline: TradingPipeline,
    ):

        self.engine = engine
        self.pipeline = pipeline

    def process_candle(
        self,
        candle: Candle,
    ) -> StrategyDecision:

        decision = (
            self.pipeline.process_candle(
                candle
            )
        )

        DecisionProcessor.process(
            self.engine,
            decision,
        )

        return decision