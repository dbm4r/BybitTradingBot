from datetime import UTC, datetime

from models.candle import Candle
from models.candle_series import CandleSeries

from strategies.engine.strategy_engine import (
    StrategyEngine,
)
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision
from strategies.orchestration.consensus_engine import (
    ConsensusEngine,
)
from strategies.orchestration.conflict_resolver import (
    ConflictResolver,
)
from strategies.orchestration.decision_aggregator import (
    DecisionAggregator,
)
from strategies.pipeline.strategy_pipeline import (
    StrategyPipeline,
)
from strategies.pipeline.strategy_stage import (
    StrategyStage,
)


class DummyStrategy(BaseStrategy):

    def __init__(
        self,
        signal,
    ):
        self._signal = signal

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
        return StrategyDecision(
            signal=self._signal,
            confidence=1.0,
            reason="test",
            strategy=self.name,
            candle=context.last_candle,
        )


def create_context():

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

    series = CandleSeries(
        symbol="BTCUSDT",
        interval="1",
        candles=[candle],
    )

    return StrategyContext(
        candles=series,
        indicators={},
    )


def test_engine():

    pipeline = StrategyPipeline()

    pipeline.add(
        StrategyStage(
            DummyStrategy(
                SignalType.OPEN_LONG,
            )
        )
    )

    engine = StrategyEngine(
        pipeline=pipeline,
        aggregator=DecisionAggregator(),
        resolver=ConflictResolver(),
        consensus=ConsensusEngine(),
    )

    decision = engine.evaluate(
        create_context(),
    )

    assert decision.signal == SignalType.OPEN_LONG