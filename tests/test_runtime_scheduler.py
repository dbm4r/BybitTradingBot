from runtime.runtime_scheduler import RuntimeScheduler
from runtime.runtime_task import RuntimeTask

print("========== RUNTIME SCHEDULER ==========\n")


class ScannerTask(RuntimeTask):

    def run(self):

        print("Scanner executed")


class HealthTask(RuntimeTask):

    def run(self):

        print("Health check executed")


scheduler = RuntimeScheduler()

scheduler.register(
    ScannerTask()
)

scheduler.register(
    HealthTask()
)

scheduler.run()