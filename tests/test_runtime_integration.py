from runtime.runtime_loop import RuntimeLoop
from runtime.runtime_scheduler import RuntimeScheduler

from runtime.tasks.execution_task import ExecutionTask
from runtime.tasks.portfolio_task import PortfolioTask
from runtime.tasks.scanner_task import ScannerTask


print("========== RUNTIME INTEGRATION ==========\n")


class DummyScanner:

    def scan(self):

        print("Scanner")


class DummyPortfolio:

    def process(self):

        print("Portfolio")


class DummyExecution:

    def process(self):

        print("Execution")


scheduler = RuntimeScheduler()

scheduler.register(
    ScannerTask(
        DummyScanner()
    )
)

scheduler.register(
    PortfolioTask(
        DummyPortfolio()
    )
)

scheduler.register(
    ExecutionTask(
        DummyExecution()
    )
)

loop = RuntimeLoop(
    scheduler
)

loop.tick()