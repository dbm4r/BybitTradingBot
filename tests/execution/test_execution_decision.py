from risk.models.risk_decision import (
    RiskDecision,
)

from execution.models.execution_decision import (
    ExecutionDecision,
)


def test_approve():

    risk = RiskDecision.approve(
        quantity=10,
    )

    decision = ExecutionDecision.approve(
        risk,
    )

    assert decision.approved

    assert decision.reason is None


def test_reject():

    risk = RiskDecision.reject(
        violations=[],
    )

    decision = ExecutionDecision.reject(
        risk,
        "Rejected",
    )

    assert not decision.approved

    assert decision.reason == "Rejected"