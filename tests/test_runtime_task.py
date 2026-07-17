from runtime.runtime_task import RuntimeTask

print("========== RUNTIME TASK ==========\n")


class DummyTask(RuntimeTask):

    def run(self):

        print("Task executed")


task = DummyTask()

task.run()