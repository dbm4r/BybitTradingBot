from datetime import UTC, datetime

from models.candle import Candle

from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)

from strategies.orchestration.decision_aggregator import (
    DecisionAggregator,
)

from strategies.pipeline.pipeline_result import (
    PipelineResult,
)


def create_decision(signal):

    candle = Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(UTC),
        open=1,
        high=1,
        low=1,
        close=1,
        volume=1,
        turnover=1,
    )

    return StrategyDecision(
        signal=signal,
        confidence=0.9,
        reason="test",
        strategy="Dummy",
        candle=candle,
    )


def test_empty():

    aggregator = DecisionAggregator()

    result = PipelineResult()

    decisions = aggregator.aggregate(
        result
    )

    assert decisions == ()


def test_single():

    aggregator = DecisionAggregator()

    result = PipelineResult()

    result.add(
        create_decision(
            SignalType.OPEN_LONG
        )
    )

    decisions = aggregator.aggregate(
        result
    )

    assert len(decisions) == 1

    assert (
        decisions[0].signal
        == SignalType.OPEN_LONG
    )


def test_multiple():

    aggregator = DecisionAggregator()

    result = PipelineResult()

    result.add(
        create_decision(
            SignalType.OPEN_LONG
        )
    )

    result.add(
        create_decision(
            SignalType.OPEN_SHORT
        )
    )

    result.add(
        create_decision(
            SignalType.HOLD
        )
    )

    decisions = aggregator.aggregate(
        result
    )

    assert len(decisions) == 3