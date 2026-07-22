from execution.framework.base_executor import (
    BaseExecutor,
)

from execution.framework.execution_pipeline import (
    ExecutionPipeline,
)


class DummyContext:

    def __init__(self):

        self.value = 2

        self.continue_execution = True


class AddOneStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        context.value += 1

        return context


class MultiplyStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        context.value *= 5

        return context


class StopStage(
    BaseExecutor,
):

    def execute(
        self,
        engine,
        context,
    ):

        context.continue_execution = False

        return context


def test_pipeline_executes_all_stages():

    pipeline = ExecutionPipeline(
        [
            AddOneStage(),
            MultiplyStage(),
        ]
    )

    context = DummyContext()

    result = pipeline.execute(
        None,
        context,
    )

    assert result.value == 15


def test_pipeline_stops_when_execution_is_cancelled():

    pipeline = ExecutionPipeline(
        [
            AddOneStage(),
            StopStage(),
            MultiplyStage(),
        ]
    )

    context = DummyContext()

    result = pipeline.execute(
        None,
        context,
    )

    assert result.value == 3

    assert result.continue_execution is False