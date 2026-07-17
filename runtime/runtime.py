from runtime.runtime_context import RuntimeContext


class TradingRuntime:

    def __init__(
        self,
        context: RuntimeContext,
    ):

        self.context = context

    def start(
        self,
    ) -> None:

        self.context.lifecycle.initialize()

        self.context.lifecycle.synchronize()

        self.context.lifecycle.start()

        if self.context.loop is not None:

            self.context.loop.tick()

    def pause(
        self,
    ) -> None:

        self.context.lifecycle.pause()

    def stop(
        self,
    ) -> None:

        self.context.lifecycle.stop()

    def error(
        self,
    ) -> None:

        self.context.lifecycle.error()

    @property
    def state(
        self,
    ):

        return self.context.session.state

    @property
    def running(
        self,
    ) -> bool:

        return self.state.value == "RUNNING"