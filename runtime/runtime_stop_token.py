class RuntimeStopToken:

    def __init__(self):

        self._running = True

    @property
    def running(
        self,
    ) -> bool:

        return self._running

    def stop(
        self,
    ) -> None:

        self._running = False

    def reset(
        self,
    ) -> None:

        self._running = True