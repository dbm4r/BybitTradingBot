from risk.engine.risk_report_builder import (
    RiskReportBuilder,
)
from risk.framework.base_risk_rule import (
    BaseRiskRule,
)
from risk.framework.risk_rule_result import (
    RiskRuleResult,
)
from risk.models.risk_violation import (
    RiskViolation,
)


class PassingRule(BaseRiskRule):

    @property
    def name(self):
        return "Passing"

    @property
    def priority(self):
        return 1

    def evaluate(self, context):
        return RiskRuleResult.success()


class FailingRule(BaseRiskRule):

    @property
    def name(self):
        return "Failing"

    @property
    def priority(self):
        return 2

    def evaluate(self, context):
        return RiskRuleResult.failure(
            RiskViolation(
                rule="CAPITAL",
                message="Insufficient capital",
            )
        )


def test_all_pass():

    report = RiskReportBuilder.build(
        (
            (
                PassingRule(),
                RiskRuleResult.success(),
            ),
        )
    )

    assert report.approved
    assert len(report.failed_rules) == 0


def test_failure():

    report = RiskReportBuilder.build(
        (
            (
                FailingRule(),
                RiskRuleResult.failure(
                    RiskViolation(
                        rule="CAPITAL",
                        message="Rejected",
                    )
                ),
            ),
        )
    )

    assert not report.approved
    assert len(report.failed_rules) == 1
    assert len(report.violations) == 1


def test_mixed_rules():

    report = RiskReportBuilder.build(
        (
            (
                PassingRule(),
                RiskRuleResult.success(),
            ),
            (
                FailingRule(),
                RiskRuleResult.failure(
                    RiskViolation(
                        rule="CAPITAL",
                        message="Rejected",
                    )
                ),
            ),
        )
    )

    assert report.approved is False

    assert report.passed_rules == (
        "Passing",
    )

    assert report.failed_rules == (
        "Failing",
    )