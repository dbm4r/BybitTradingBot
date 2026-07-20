from datetime import UTC, datetime

from models.candle import Candle

from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)

from strategies.orchestration.conflict_resolver import (
    ConflictResolver,
)


def decision(signal, confidence=1.0):

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

    resolver = ConflictResolver()

    grouped = resolver.resolve(())

    assert grouped == {}


def test_single_signal():

    resolver = ConflictResolver()

    grouped = resolver.resolve(
        (
            decision(
                SignalType.OPEN_LONG
            ),
        )
    )

    assert len(grouped) == 1

    assert SignalType.OPEN_LONG in grouped

    assert len(
        grouped[
            SignalType.OPEN_LONG
        ]
    ) == 1


def test_group_same_signal():

    resolver = ConflictResolver()

    grouped = resolver.resolve(
        (
            decision(
                SignalType.OPEN_LONG
            ),
            decision(
                SignalType.OPEN_LONG
            ),
            decision(
                SignalType.OPEN_LONG
            ),
        )
    )

    assert len(
        grouped[
            SignalType.OPEN_LONG
        ]
    ) == 3


def test_group_multiple_signals():

    resolver = ConflictResolver()

    grouped = resolver.resolve(
        (
            decision(
                SignalType.OPEN_LONG
            ),
            decision(
                SignalType.OPEN_SHORT
            ),
            decision(
                SignalType.HOLD
            ),
        )
    )

    assert len(grouped) == 3

    assert SignalType.OPEN_LONG in grouped

    assert SignalType.OPEN_SHORT in grouped

    assert SignalType.HOLD in grouped