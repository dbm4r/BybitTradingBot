from dataclasses import dataclass

from data.validation.gap_report import GapReport


@dataclass(slots=True)
class GapRepairRequest:

    symbol: str

    interval: str

    report: GapReport

    filename: str