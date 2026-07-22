from orders.lifecycle.order_state import (
    OrderState,
)


def test_order_states_exist():

    assert OrderState.CREATED.value == "CREATED"

    assert OrderState.SUBMITTED.value == "SUBMITTED"

    assert OrderState.ACCEPTED.value == "ACCEPTED"

    assert OrderState.PARTIALLY_FILLED.value == (
        "PARTIALLY_FILLED"
    )

    assert OrderState.FILLED.value == "FILLED"

    assert OrderState.CANCELLED.value == "CANCELLED"

    assert OrderState.REJECTED.value == "REJECTED"

    assert OrderState.EXPIRED.value == "EXPIRED"

    assert OrderState.AMENDED.value == "AMENDED"