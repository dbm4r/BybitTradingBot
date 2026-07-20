from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import StrategyDecision

from strategies.pipeline.strategy_pipeline_builder import (
    StrategyPipelineBuilder,
)


class DummyStrategy(BaseStrategy):

    def __init__(self, name):

        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def parameters(self):
        return {}

    @property
    def indicators(self):
        return ()

    @property
    def supported_regimes(self):
        return {}

    @property
    def requires_higher_timeframe_confirmation(self):
        return False

    @property
    def confirmation_timeframes(self):
        return ()

    def evaluate(
        self,
        context,
    ):

        return StrategyDecision.hold(
            candle=context.last_candle,
            strategy=self.name,
            reason="test",
        )


def test_add():

    pipeline = (
        StrategyPipelineBuilder()
        .add(
            DummyStrategy(
                "SMA"
            )
        )
        .build()
    )

    assert pipeline.count == 1


def test_add_many():

    pipeline = (
        StrategyPipelineBuilder()
        .add_many(
            DummyStrategy("SMA"),
            DummyStrategy("EMA"),
            DummyStrategy("RSI"),
        )
        .build()
    )

    assert pipeline.count == 3


def test_builder_chain():

    builder = (
        StrategyPipelineBuilder()
        .add(
            DummyStrategy(
                "SMA"
            )
        )
        .add(
            DummyStrategy(
                "EMA"
            )
        )
    )

    pipeline = builder.build()

    assert pipeline.count == 2


def test_priorities():

    pipeline = (
        StrategyPipelineBuilder()
        .add(
            DummyStrategy("SMA"),
            priority=10,
        )
        .add(
            DummyStrategy("EMA"),
            priority=20,
        )
        .build()
    )

    assert pipeline.stages[0].priority == 10

    assert pipeline.stages[1].priority == 20