from runtime.runtime_loop import RuntimeLoop
from runtime.runtime_scheduler import RuntimeScheduler
from runtime.runtime_task import RuntimeTask

print("========== RUNTIME LOOP ==========\n")


class ScannerTask(RuntimeTask):

    def run(self):

        print("Scanner")


class PortfolioTask(RuntimeTask):

    def run(self):

        print("Portfolio")


scheduler = RuntimeScheduler()

scheduler.register(
    ScannerTask()
)

scheduler.register(
    PortfolioTask()
)

loop = RuntimeLoop(
    scheduler
)

loop.tick()