from runtime.runtime_scheduler import RuntimeScheduler


class RuntimeLoop:

    def __init__(
        self,
        scheduler: RuntimeScheduler,
    ):

        self.scheduler = scheduler

    def tick(
        self,
    ) -> None:

        self.scheduler.run()