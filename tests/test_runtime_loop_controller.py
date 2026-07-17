from runtime.runtime_loop import RuntimeLoop
from runtime.runtime_runner import RuntimeLoopController
from runtime.runtime_scheduler import RuntimeScheduler
from runtime.runtime_sleep import RuntimeSleep
from runtime.runtime_stop_token import RuntimeStopToken

print("========== LOOP CONTROLLER ==========\n")

scheduler = RuntimeScheduler()

loop = RuntimeLoop(
    scheduler
)

token = RuntimeStopToken()

sleep = RuntimeSleep()

controller = RuntimeLoopController(
    loop=loop,
    token=token,
    sleeper=sleep,
)

print(token.running)

controller.stop()

print(token.running)