from runtime.tasks.execution_task import ExecutionTask


print("========== EXECUTION TASK ==========\n")


class DummyExecution:

    def __init__(self):

        self.executed = False

    def process(
        self,
    ) -> None:

        self.executed = True

        print("Processing execution...")


execution = DummyExecution()

task = ExecutionTask(
    execution
)

task.run()

print()

print("Executed:")
print(execution.executed)