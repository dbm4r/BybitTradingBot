from dataclasses import dataclass

from execution.models.order_result import (
    OrderResult,
)


@dataclass(
    slots=True,
)
class ExecutionReport:

    success: bool

    order: OrderResult | None

    message: str | None = None