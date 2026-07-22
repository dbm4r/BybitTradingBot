from datetime import datetime

from orders.events.order_event import (
    OrderEvent,
)

from orders.lifecycle.order_state_machine import (
    OrderStateMachine,
)


class OrderTransitionService:

    @staticmethod
    def initialize(
        order,
    ):

        order.history.append(
            OrderEvent(
                state=order.status,
                timestamp=datetime.now(),
            )
        )

        return order

    @staticmethod
    def transition(
        order,
        target,
    ):

        if not OrderStateMachine.can_transition(
            order.status,
            target,
        ):
            raise ValueError(
                f"Invalid transition "
                f"{order.status.name}"
                f" -> "
                f"{target.name}"
            )

        order.status = target

        order.history.append(
            OrderEvent(
                state=target,
                timestamp=datetime.now(),
            )
        )

        return order