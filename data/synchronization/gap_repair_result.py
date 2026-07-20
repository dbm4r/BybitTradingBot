from dataclasses import dataclass


@dataclass(slots=True)
class GapRepairResult:

    repaired: bool

    repaired_gaps: int

    downloaded_candles: int