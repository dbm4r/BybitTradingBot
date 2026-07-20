from datetime import UTC, datetime

from models.candle import Candle
from models.candle_series import CandleSeries

from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision

from strategies.pipeline.strategy_pipeline import (
    StrategyPipeline,
)
from strategies.pipeline.strategy_stage import (
    StrategyStage,
)


class DummyStrategy(BaseStrategy):

    def __init__(
        self,
        name: str,
        signal: SignalType,
    ):

        self._name = name
        self._signal = signal

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

        return StrategyDecision(
            signal=self._signal,
            confidence=1.0,
            reason=self._name,
            strategy=self._name,
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


def test_pipeline_single_strategy():

    pipeline = StrategyPipeline()

    pipeline.add(
        StrategyStage(
            strategy=DummyStrategy(
                "SMA",
                SignalType.OPEN_LONG,
            )
        )
    )

    result = pipeline.run(
        create_context()
    )

    assert result.count == 1

    assert (
        result.decisions[0].signal
        == SignalType.OPEN_LONG
    )


def test_pipeline_multiple_strategies():

    pipeline = StrategyPipeline()

    pipeline.add_many(
        StrategyStage(
            DummyStrategy(
                "SMA",
                SignalType.OPEN_LONG,
            )
        ),
        StrategyStage(
            DummyStrategy(
                "EMA",
                SignalType.OPEN_SHORT,
            )
        ),
        StrategyStage(
            DummyStrategy(
                "RSI",
                SignalType.HOLD,
            )
        ),
    )

    result = pipeline.run(
        create_context()
    )

    assert result.count == 3


def test_disabled_stage():

    pipeline = StrategyPipeline()

    pipeline.add(
        StrategyStage(
            strategy=DummyStrategy(
                "EMA",
                SignalType.OPEN_LONG,
            ),
            enabled=False,
        )
    )

    result = pipeline.run(
        create_context()
    )

    assert result.empty


def test_pipeline_clear():

    pipeline = StrategyPipeline()

    pipeline.add(
        StrategyStage(
            DummyStrategy(
                "SMA",
                SignalType.OPEN_LONG,
            )
        )
    )

    pipeline.clear()

    assert pipeline.count == 0