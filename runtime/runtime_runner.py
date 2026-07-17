from runtime.runtime_loop import RuntimeLoop
from runtime.runtime_sleep import RuntimeSleep
from runtime.runtime_stop_token import RuntimeStopToken


class RuntimeRunner:

    def __init__(
        self,
        loop: RuntimeLoop,
        token: RuntimeStopToken,
        sleeper: RuntimeSleep,
        interval: float = 1.0,
    ):

        self.loop = loop
        self.token = token
        self.sleeper = sleeper
        self.interval = interval

    def run(
        self,
    ) -> None:

        while self.token.running:

            self.step()

    def step(
        self,
    ) -> None:

        self.loop.tick()

        self.sleeper.wait(
            self.interval
        )

    def stop(
        self,
    ) -> None:

        self.token.stop()

    def reset(
        self,
    ) -> None:

        self.token.reset()