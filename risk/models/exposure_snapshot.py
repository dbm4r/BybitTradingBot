from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ExposureSnapshot:

    total_exposure: float

    long_exposure: float

    short_exposure: float

    open_positions: int

    leverage: float = 1.0

    @property
    def net_exposure(
        self,
    ) -> float:

        return (
            self.long_exposure
            - self.short_exposure
        )

    @property
    def gross_exposure(
        self,
    ) -> float:

        return (
            self.long_exposure
            + self.short_exposure
        )