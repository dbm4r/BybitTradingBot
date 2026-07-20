from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class PositionSize:

    quantity: float

    risk_amount: float

    risk_percent: float

    entry_price: float

    stop_price: float

    @property
    def notional(
        self,
    ) -> float:

        return (
            self.quantity
            * self.entry_price
        )