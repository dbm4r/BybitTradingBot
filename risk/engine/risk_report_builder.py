from risk.framework.base_risk_rule import (
    BaseRiskRule,
)

from risk.framework.risk_rule_result import (
    RiskRuleResult,
)

from risk.models.risk_report import (
    RiskReport,
)


class RiskReportBuilder:

    @staticmethod
    def build(
        evaluations: tuple[
            tuple[
                BaseRiskRule,
                RiskRuleResult,
            ],
            ...
        ],
    ) -> RiskReport:

        passed = []

        failed = []

        violations = []

        for rule, result in evaluations:

            if result.passed:

                passed.append(
                    rule.name
                )

            else:

                failed.append(
                    rule.name
                )

                violations.extend(
                    result.violations
                )

        return RiskReport(
            passed_rules=tuple(
                passed
            ),
            failed_rules=tuple(
                failed
            ),
            violations=tuple(
                violations
            ),
        )