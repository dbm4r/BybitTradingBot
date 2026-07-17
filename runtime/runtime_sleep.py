import time


class RuntimeSleep:

    def wait(
        self,
        seconds: float,
    ) -> None:

        time.sleep(
            seconds
        )