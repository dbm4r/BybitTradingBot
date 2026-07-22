from dataclasses import dataclass

from backtesting.portfolio import (
    Portfolio,
)

from exchange.exchange_result import (
    ExchangeResult,
)

from execution.models.execution_decision import (
    ExecutionDecision,
)

from orders.order import (
    Order,
)

from risk.models.position_size import (
    PositionSize,
)

from strategies.framework.strategy_decision import (
    StrategyDecision,
)


@dataclass(slots=True)
class ExecutionContext:

    # ------------------------------------------
    # Input
    # ------------------------------------------

    decision: StrategyDecision

    portfolio: Portfolio

    # ------------------------------------------
    # Capital
    # ------------------------------------------

    available_capital: float

    fee: float

    slippage: float

    # ------------------------------------------
    # Prices
    # ------------------------------------------

    entry_price: float

    stop_price: float

    take_profit_price: float

    # ------------------------------------------
    # Position
    # ------------------------------------------

    position_size: PositionSize

    # ------------------------------------------
    # Pipeline State
    # ------------------------------------------

    risk_decision: ExecutionDecision | None = None

    order: Order | None = None

    exchange_result: ExchangeResult | None = None

    continue_execution: bool = True

    failure_reason: str | None = None