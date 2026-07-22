from execution.framework.execution_pipeline import (
    ExecutionPipeline,
)

from execution.framework.stages.risk_stage import (
    RiskStage,
)

from execution.framework.stages.validation_stage import (
    ValidationStage,
)

from execution.framework.stages.order_creation_stage import (
    OrderCreationStage,
)

from execution.framework.stages.submission_stage import (
    SubmissionStage,
)

from execution.framework.stages.fill_stage import (
    FillStage,
)


class ExecutionPipelineBuilder:

    def __init__(
        self,
    ):

        self._stages = []

    def add_stage(
        self,
        stage,
    ):

        self._stages.append(
            stage,
        )

        return self
    def default_entry_pipeline(
        self,
    ):

        return (
            self.add_stage(
                RiskStage(),
            )
            .add_stage(
                ValidationStage(),
            )
            .add_stage(
                OrderCreationStage(),
            )
            .add_stage(
                SubmissionStage(),
            )
            .add_stage(
                FillStage(),
            )
        )

    def build(
        self,
    ):

        return ExecutionPipeline(
            self._stages,
        )