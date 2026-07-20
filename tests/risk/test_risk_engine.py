from datetime import UTC, datetime

from models.candle import Candle
from portfolio.portfolio_manager import PortfolioManager

from risk.engine.risk_engine import RiskEngine
from risk.framework.base_risk_rule import BaseRiskRule
from risk.framework.risk_pipeline import RiskPipeline
from risk.framework.risk_rule_result import RiskRuleResult
from risk.models.exposure_snapshot import ExposureSnapshot
from risk.models.position_size import PositionSize
from risk.models.risk_budget import RiskBudget
from risk.models.risk_context import RiskContext
from risk.models.risk_violation import RiskViolation

from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import StrategyDecision


class PassingRule(BaseRiskRule):

    @property
    def name(self):
        return "PASS"

    @property
    def priority(self):
        return 1

    def evaluate(self, context):
        return RiskRuleResult.success()


class FailingRule(BaseRiskRule):

    @property
    def name(self):
        return "FAIL"

    @property
    def priority(self):
        return 1

    def evaluate(self, context):

        return RiskRuleResult.failure(
            RiskViolation(
                rule="FAIL",
                message="Rejected",
            )
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
            risk_amount=10,
            risk_percent=0.01,
            entry_price=1,
            stop_price=0.9,
        ),
        portfolio=PortfolioManager(),
        available_capital=1000,
        exposure=ExposureSnapshot(
            total_exposure=0,
            long_exposure=0,
            short_exposure=0,
            open_positions=0,
        ),
        budget=RiskBudget(
            total=100,
        ),
    )


def test_engine_approves():

    pipeline = RiskPipeline()

    pipeline.add(
        PassingRule()
    )

    engine = RiskEngine(
        pipeline
    )

    result = engine.evaluate(
        create_context()
    )

    assert result.approved
    assert result.quantity == 1


def test_engine_rejects():

    pipeline = RiskPipeline()

    pipeline.add(
        FailingRule()
    )

    engine = RiskEngine(
        pipeline
    )

    result = engine.evaluate(
        create_context()
    )

    assert not result.approved
    assert len(result.violations) == 1