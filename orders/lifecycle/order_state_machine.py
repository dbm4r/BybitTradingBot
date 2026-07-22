from orders.lifecycle.order_state import (
    OrderState,
)


class OrderStateMachine:

    _allowed = {

        OrderState.CREATED: {
            OrderState.SUBMITTED,
        },

        OrderState.SUBMITTED: {
            OrderState.ACCEPTED,
            OrderState.REJECTED,
            OrderState.CANCELLED,
        },

        OrderState.ACCEPTED: {
            OrderState.PARTIALLY_FILLED,
            OrderState.FILLED,
            OrderState.CANCELLED,
            OrderState.EXPIRED,
            OrderState.AMENDED,
        },

        OrderState.PARTIALLY_FILLED: {
            OrderState.PARTIALLY_FILLED,
            OrderState.FILLED,
            OrderState.CANCELLED,
        },

        OrderState.AMENDED: {
            OrderState.ACCEPTED,
        },

        OrderState.FILLED: set(),

        OrderState.CANCELLED: set(),

        OrderState.REJECTED: set(),

        OrderState.EXPIRED: set(),
    }

    @classmethod
    def can_transition(
        cls,
        current,
        target,
    ):

        return (
            target
            in cls._allowed.get(
                current,
                set(),
            )
        )