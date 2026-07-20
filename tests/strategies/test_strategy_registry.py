from indicators.ema import (
    ExponentialMovingAverage,
)

from strategies.framework.base_strategy import (
    BaseStrategy,
)
from strategies.framework.signal_type import (
    SignalType,
)
from strategies.framework.strategy_decision import (
    StrategyDecision,
)

from strategies.registry.strategy_metadata import (
    StrategyMetadata,
)
from strategies.registry.strategy_registry import (
    StrategyRegistry,
)


class DummyStrategy(BaseStrategy):

    @property
    def name(self):
        return "Dummy"

    @property
    def parameters(self):
        return {}

    @property
    def indicators(self):
        return (
            ExponentialMovingAverage(20),
        )

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

        return StrategyDecision(
            signal=SignalType.HOLD,
            confidence=1.0,
            reason="dummy",
            strategy=self.name,
            candle=context.last_candle,
        )


def create_metadata():

    return StrategyMetadata(
        name="Dummy",
        category="Test",
        tags=("test",),
    )


def test_register():

    registry = StrategyRegistry()

    registry.register(
        DummyStrategy(),
        create_metadata(),
    )

    assert registry.count == 1

    assert registry.contains(
        "Dummy"
    )


def test_unregister():

    registry = StrategyRegistry()

    registry.register(
        DummyStrategy(),
        create_metadata(),
    )

    registry.unregister(
        "Dummy"
    )

    assert registry.count == 0


def test_get_strategy():

    registry = StrategyRegistry()

    strategy = DummyStrategy()

    registry.register(
        strategy,
        create_metadata(),
    )

    assert (
        registry.get("Dummy")
        is strategy
    )


def test_metadata():

    registry = StrategyRegistry()

    metadata = create_metadata()

    registry.register(
        DummyStrategy(),
        metadata,
    )

    assert (
        registry.metadata("Dummy")
        == metadata
    )


def test_category():

    registry = StrategyRegistry()

    registry.register(
        DummyStrategy(),
        create_metadata(),
    )

    assert len(
        registry.by_category(
            "Test"
        )
    ) == 1


def test_tag():

    registry = StrategyRegistry()

    registry.register(
        DummyStrategy(),
        create_metadata(),
    )

    assert len(
        registry.by_tag(
            "test"
        )
    ) == 1


def test_enabled():

    registry = StrategyRegistry()

    registry.register(
        DummyStrategy(),
        create_metadata(),
    )

    assert len(
        registry.enabled()
    ) == 1


def test_clear():

    registry = StrategyRegistry()

    registry.register(
        DummyStrategy(),
        create_metadata(),
    )

    registry.clear()

    assert registry.count == 0