import math

from risk.models.position_size import (
    PositionSize,
)

from risk.sizing.fixed_risk_sizer import (
    FixedRiskSizer,
)


def test_fixed_risk_quantity():

    sizer = FixedRiskSizer()

    position = sizer.calculate(
        available_capital=10000,
        risk_percent=0.02,
        entry_price=100,
        stop_price=95,
    )

    assert isinstance(
        position,
        PositionSize,
    )

    assert math.isclose(
        position.quantity,
        40.0,
    )

    assert position.risk_amount == 200

    assert position.risk_percent == 0.02


def test_zero_risk_distance():

    sizer = FixedRiskSizer()

    position = sizer.calculate(
        available_capital=10000,
        risk_percent=0.02,
        entry_price=100,
        stop_price=100,
    )

    assert position.quantity == 0.0

    assert position.risk_amount == 0.0


def test_notional():

    sizer = FixedRiskSizer()

    position = sizer.calculate(
        available_capital=5000,
        risk_percent=0.01,
        entry_price=50,
        stop_price=48,
    )

    assert math.isclose(
        position.notional,
        position.quantity * 50,
    )


def test_name():

    sizer = FixedRiskSizer()

    assert sizer.name == "Fixed Risk"