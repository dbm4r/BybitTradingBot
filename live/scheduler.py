import time
from datetime import datetime, UTC


class Scheduler:

    @staticmethod
    def wait_for_next_candle(
        interval_minutes: int
    ):

        now = datetime.now(UTC)

        seconds = (
            now.minute * 60
            + now.second
        )

        interval_seconds = (
            interval_minutes * 60
        )

        wait = (
            interval_seconds
            - (seconds % interval_seconds)
        )

        if wait == 0:
            wait = interval_seconds

        print(
            f"Waiting {wait} seconds..."
        )

        time.sleep(wait)