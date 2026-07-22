from orders.lifecycle.order_state import (
    OrderState,
)
from orders.lifecycle.order_state_machine import (
    OrderStateMachine,
)


def test_created_to_submitted():

    assert OrderStateMachine.can_transition(
        OrderState.CREATED,
        OrderState.SUBMITTED,
    )


def test_submitted_to_accepted():

    assert OrderStateMachine.can_transition(
        OrderState.SUBMITTED,
        OrderState.ACCEPTED,
    )


def test_accepted_to_filled():

    assert OrderStateMachine.can_transition(
        OrderState.ACCEPTED,
        OrderState.FILLED,
    )


def test_created_to_filled_not_allowed():

    assert not OrderStateMachine.can_transition(
        OrderState.CREATED,
        OrderState.FILLED,
    )


def test_filled_is_terminal():

    assert not OrderStateMachine.can_transition(
        OrderState.FILLED,
        OrderState.ACCEPTED,
    )