from dataclasses import dataclass


@dataclass(slots=True)
class IndicatorResult:
    name: str
    output_name: str
    values: list[float | None]
    parameters: dict[str, int | float | str]

    @property
    def last(self) -> float | None:
        if not self.values:
            return None
        return self.values[-1]

    @property
    def first(self) -> float | None:
        if not self.values:
            return None
        return self.values[0]

    @property
    def count(self) -> int:
        return len(self.values)

    @property
    def is_empty(self) -> bool:
        return len(self.values) == 0