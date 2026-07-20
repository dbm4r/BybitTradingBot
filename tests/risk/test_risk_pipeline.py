from datetime import UTC, datetime

from models.candle import Candle
from portfolio.portfolio_manager import PortfolioManager

from risk.framework.base_risk_rule import BaseRiskRule
from risk.framework.risk_pipeline import RiskPipeline
from risk.framework.risk_rule_result import RiskRuleResult
from risk.models.exposure_snapshot import ExposureSnapshot
from risk.models.position_size import PositionSize
from risk.models.risk_budget import RiskBudget
from risk.models.risk_context import RiskContext
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import StrategyDecision


class DummyRule(BaseRiskRule):

    def __init__(self, name: str, priority: int):

        self._name = name
        self._priority = priority

    @property
    def name(self):

        return self._name

    @property
    def priority(self):

        return self._priority

    def evaluate(
        self,
        context,
    ):

        return RiskRuleResult.success()


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

    decision = StrategyDecision(
        signal=SignalType.OPEN_LONG,
        confidence=1,
        reason="test",
        strategy="Dummy",
        candle=candle,
    )

    return RiskContext(
        decision=decision,
        position_size=PositionSize(
            quantity=1,
            risk_amount=100,
            risk_percent=0.01,
            entry_price=1,
            stop_price=0.9,
        ),
        portfolio=PortfolioManager(),
        available_capital=10000,
        exposure=ExposureSnapshot(
            total_exposure=0,
            long_exposure=0,
            short_exposure=0,
            open_positions=0,
        ),
        budget=RiskBudget(
            total=1000,
        ),
    )


def test_add_rule():

    pipeline = RiskPipeline()

    pipeline.add(
        DummyRule(
            "B",
            20,
        )
    )

    assert pipeline.count == 1


def test_sort_by_priority():

    pipeline = RiskPipeline()

    pipeline.add_many(
        DummyRule(
            "Late",
            20,
        ),
        DummyRule(
            "Early",
            10,
        ),
    )

    assert pipeline.rules[0].name == "Early"


def test_evaluate():

    pipeline = RiskPipeline()

    pipeline.add(
        DummyRule(
            "Rule",
            1,
        )
    )

    results = pipeline.evaluate(
        create_context(),
    )

    assert len(results) == 1
    assert results[0].passed