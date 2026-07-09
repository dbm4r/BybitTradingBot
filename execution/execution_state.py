from dataclasses import dataclass, field


@dataclass
class ExecutionState:

    pending_orders: dict = field(
        default_factory=dict
    )

    active_orders: dict = field(
        default_factory=dict
    )

    completed_orders: dict = field(
        default_factory=dict
    )