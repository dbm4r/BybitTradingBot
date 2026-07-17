from runtime.runtime_task import RuntimeTask


class ExecutionTask(RuntimeTask):

    def __init__(
        self,
        execution,
    ):

        self.execution = execution

    def run(
        self,
    ) -> None:

        self.execution.process()