from risk.engine.risk_report_builder import (
    RiskReportBuilder,
)
from risk.framework.risk_pipeline import (
    RiskPipeline,
)
from risk.models.risk_context import (
    RiskContext,
)
from risk.models.risk_decision import (
    RiskDecision,
)


class RiskEngine:

    def __init__(
        self,
        pipeline: RiskPipeline,
    ):

        self.pipeline = pipeline

    def evaluate(
        self,
        context: RiskContext,
    ) -> RiskDecision:

        evaluations = tuple(

            (
                rule,
                rule.evaluate(
                    context,
                ),
            )

            for rule in self.pipeline.rules
        )

        report = (
            RiskReportBuilder.build(
                evaluations,
            )
        )

        if report.approved:

            return RiskDecision.approve(
                quantity=context.position_size.quantity,
            )

        return RiskDecision.reject(
            violations=report.violations,
        )