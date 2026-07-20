from enum import Enum


class Interval(Enum):

    M1 = ("1", 60_000)
    M3 = ("3", 180_000)
    M5 = ("5", 300_000)
    M15 = ("15", 900_000)
    M30 = ("30", 1_800_000)

    H1 = ("60", 3_600_000)
    H2 = ("120", 7_200_000)
    H4 = ("240", 14_400_000)
    H6 = ("360", 21_600_000)
    H12 = ("720", 43_200_000)

    D1 = ("D", 86_400_000)
    W1 = ("W", 604_800_000)
    M1_MONTH = ("M", 2_592_000_000)

    def __init__(
        self,
        code: str,
        milliseconds: int,
    ):

        self.code = code
        self.milliseconds = milliseconds

    @classmethod
    def from_code(
        cls,
        code: str,
    ):

        for interval in cls:

            if interval.code == code:
                return interval

        raise ValueError(
            f"Unsupported interval: {code}"
        )