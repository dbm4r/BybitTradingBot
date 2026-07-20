from risk.models.position_size import (
    PositionSize,
)

from risk.sizing.base_position_sizer import (
    BasePositionSizer,
)


class FixedRiskSizer(
    BasePositionSizer,
):

    @property
    def name(
        self,
    ) -> str:

        return "Fixed Risk"


    def calculate(
        self,
        available_capital: float,
        risk_percent: float,
        entry_price: float,
        stop_price: float,
    ) -> PositionSize:

        risk_per_unit = abs(
            entry_price - stop_price
        )

        if risk_per_unit <= 0:

            return PositionSize(
                quantity=0.0,
                risk_amount=0.0,
                risk_percent=risk_percent,
                entry_price=entry_price,
                stop_price=stop_price,
            )


        risk_amount = (
            available_capital
            * risk_percent
        )


        quantity = (
            risk_amount
            / risk_per_unit
        )


        return PositionSize(
            quantity=quantity,
            risk_amount=risk_amount,
            risk_percent=risk_percent,
            entry_price=entry_price,
            stop_price=stop_price,
        )