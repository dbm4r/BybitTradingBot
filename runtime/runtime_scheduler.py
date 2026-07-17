from runtime.runtime_task import RuntimeTask


class RuntimeScheduler:

    def __init__(self):

        self.tasks: list[RuntimeTask] = []

    def register(
        self,
        task: RuntimeTask,
    ) -> None:

        self.tasks.append(task)

    def run(
        self,
    ) -> None:

        for task in self.tasks:

            task.run()