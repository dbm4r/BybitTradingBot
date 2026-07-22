from orders.lifecycle.order_state import (
    OrderState,
)

from orders.services.order_transition_service import (
    OrderTransitionService,
)


class OrderLifecycleManager:

    @staticmethod
    def initialize(
        order,
    ):

        return OrderTransitionService.initialize(
            order,
        )

    @staticmethod
    def transition(
        order,
        target,
    ):

        return OrderTransitionService.transition(
            order,
            target,
        )

    @staticmethod
    def is_active(
        order,
    ):

        return order.status in {
            OrderState.SUBMITTED,
            OrderState.ACCEPTED,
            OrderState.PARTIALLY_FILLED,
        }

    @staticmethod
    def is_terminal(
        order,
    ):

        return order.status in {
            OrderState.FILLED,
            OrderState.CANCELLED,
            OrderState.REJECTED,
            OrderState.EXPIRED,
        }

    @staticmethod
    def can_fill(
        order,
    ):

        return order.status in {
            OrderState.ACCEPTED,
            OrderState.PARTIALLY_FILLED,
        }

    @staticmethod
    def can_cancel(
        order,
    ):

        return order.status in {
            OrderState.SUBMITTED,
            OrderState.ACCEPTED,
            OrderState.PARTIALLY_FILLED,
        }

    @staticmethod
    def can_amend(
        order,
    ):

        return order.status == OrderState.ACCEPTED

    @staticmethod
    def can_expire(
        order,
    ):

        return order.status == OrderState.ACCEPTED