from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.framework.execution_pipeline_builder import (
    ExecutionPipelineBuilder,
)


class DummyStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        return context


def test_builder_creates_pipeline():

    pipeline = (
        ExecutionPipelineBuilder()
        .add_stage(
            DummyStage(),
        )
        .build()
    )

    assert len(
        pipeline.stages
    ) == 1

    assert isinstance(
        pipeline.stages[0],
        DummyStage,
    )