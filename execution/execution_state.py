from dataclasses import dataclass, field


@dataclass
class ExecutionState:

    _pending_orders: dict = field(
        default_factory=dict,
    )

    _active_orders: dict = field(
        default_factory=dict,
    )

    _completed_orders: dict = field(
        default_factory=dict,
    )

    def register_pending_order(
        self,
        order,
    ):

        self._pending_orders[
            order.exchange_order_id
        ] = order

    def unregister_pending_order(
        self,
        exchange_order_id,
    ):

        return self._pending_orders.pop(
            exchange_order_id,
            None,
        )

    def get_pending_order(
        self,
        exchange_order_id,
    ):

        return self._pending_orders.get(
            exchange_order_id,
        )

    def has_pending_order(
        self,
        exchange_order_id,
    ):

        return (
            exchange_order_id
            in self._pending_orders
        )

    def pending_orders(
        self,
    ):

        return tuple(
            self._pending_orders.values()
        )

    def clear_pending_orders(
        self,
    ):

        self._pending_orders.clear()