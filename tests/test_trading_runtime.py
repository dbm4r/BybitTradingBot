from runtime.runtime import TradingRuntime
from runtime.runtime_context import RuntimeContext
from runtime.runtime_lifecycle import RuntimeLifecycle
from runtime.runtime_session import RuntimeSession
from runtime.runtime_settings import RuntimeSettings
from runtime.runtime_scheduler import RuntimeScheduler
from runtime.runtime_loop import RuntimeLoop
from runtime.runtime_task import RuntimeTask


print("========== TRADING RUNTIME ==========\n")


class ScannerTask(RuntimeTask):

    def run(self):

        print("Scanner Task Executed")


session = RuntimeSession()

lifecycle = RuntimeLifecycle(
    session
)

settings = RuntimeSettings()

scheduler = RuntimeScheduler()

scheduler.register(
    ScannerTask()
)

loop = RuntimeLoop(
    scheduler
)

context = RuntimeContext(
    session=session,
    lifecycle=lifecycle,
    settings=settings,
    scheduler=scheduler,
    loop=loop,
)

runtime = TradingRuntime(
    context
)

print(runtime.state.value)
print(runtime.running)

print()

runtime.start()

print()

print(runtime.state.value)
print(runtime.running)

print()

runtime.pause()

print(runtime.state.value)
print(runtime.running)

print()

runtime.stop()

print(runtime.state.value)
print(runtime.running)