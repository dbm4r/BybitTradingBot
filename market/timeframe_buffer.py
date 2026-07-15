from datetime import datetime

from models.candle import Candle


class TimeframeBuffer:

    def __init__(self):

        self.bucket: datetime | None = None

        self.candles: list[Candle] = []

    def start(
        self,
        bucket: datetime,
    ) -> None:

        self.bucket = bucket

        self.candles.clear()

    def add(
        self,
        candle: Candle,
    ) -> None:

        self.candles.append(candle)

    def clear(
        self,
    ) -> None:

        self.bucket = None

        self.candles.clear()

    @property
    def is_empty(
        self,
    ) -> bool:

        return len(self.candles) == 0

    @property
    def count(
        self,
    ) -> int:

        return len(self.candles)