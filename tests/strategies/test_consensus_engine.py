from datetime import UTC, datetime

import pytest

from models.candle import Candle

from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)

from strategies.orchestration.consensus_engine import (
    ConsensusEngine,
)


def decision(
    signal,
    confidence,
):

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
        confidence=confidence,
        reason="test",
        strategy="Dummy",
        candle=candle,
    )


def test_empty():

    engine = ConsensusEngine()

    with pytest.raises(
        ValueError,
    ):

        engine.decide(
            {}
        )


def test_majority_vote():

    engine = ConsensusEngine()

    grouped = {

        SignalType.OPEN_LONG: (

            decision(
                SignalType.OPEN_LONG,
                0.80,
            ),

            decision(
                SignalType.OPEN_LONG,
                0.90,
            ),
        ),

        SignalType.OPEN_SHORT: (

            decision(
                SignalType.OPEN_SHORT,
                0.99,
            ),
        ),
    }

    result = engine.decide(
        grouped
    )

    assert (
        result.signal
        == SignalType.OPEN_LONG
    )


def test_hold_is_ignored():

    engine = ConsensusEngine()

    grouped = {

        SignalType.HOLD: (

            decision(
                SignalType.HOLD,
                1.0,
            ),

            decision(
                SignalType.HOLD,
                1.0,
            ),
        ),

        SignalType.OPEN_LONG: (

            decision(
                SignalType.OPEN_LONG,
                0.60,
            ),
        ),
    }

    result = engine.decide(
        grouped
    )

    assert (
        result.signal
        == SignalType.OPEN_LONG
    )


def test_only_hold():

    engine = ConsensusEngine()

    grouped = {

        SignalType.HOLD: (

            decision(
                SignalType.HOLD,
                0.90,
            ),

            decision(
                SignalType.HOLD,
                0.95,
            ),
        )
    }

    result = engine.decide(
        grouped
    )

    assert (
        result.signal
        == SignalType.HOLD
    )

    assert (
        result.confidence
        == 0.95
    )


def test_tie_highest_average_confidence():

    engine = ConsensusEngine()

    grouped = {

        SignalType.OPEN_LONG: (

            decision(
                SignalType.OPEN_LONG,
                0.70,
            ),

            decision(
                SignalType.OPEN_LONG,
                0.80,
            ),
        ),

        SignalType.OPEN_SHORT: (

            decision(
                SignalType.OPEN_SHORT,
                0.95,
            ),

            decision(
                SignalType.OPEN_SHORT,
                0.90,
            ),
        ),
    }

    result = engine.decide(
        grouped
    )

    assert (
        result.signal
        == SignalType.OPEN_SHORT
    )

    assert (
        result.confidence
        == 0.95
    )