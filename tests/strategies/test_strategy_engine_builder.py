from strategies.engine.strategy_engine import (
    StrategyEngine,
)
from strategies.engine.strategy_engine_builder import (
    StrategyEngineBuilder,
)
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.strategy_decision import StrategyDecision


class DummyStrategy(BaseStrategy):

    @property
    def name(self):
        return "Dummy"

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
            reason="builder",
        )


def test_builder():

    engine = (
        StrategyEngineBuilder()
        .add(
            DummyStrategy(),
        )
        .build()
    )

    assert isinstance(
        engine,
        StrategyEngine,
    )


def test_multiple_strategies():

    engine = (
        StrategyEngineBuilder()
        .add(
            DummyStrategy(),
        )
        .add(
            DummyStrategy(),
        )
        .build()
    )

    assert isinstance(
        engine,
        StrategyEngine,
    )