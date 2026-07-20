from dataclasses import dataclass

from data.validation.missing_range import (
    MissingRange,
)


@dataclass(slots=True)
class GapReport:

    has_gaps: bool

    gaps: list[MissingRange]

    total_missing_candles: int