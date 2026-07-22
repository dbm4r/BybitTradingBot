from dataclasses import dataclass

from backtesting.portfolio import (
    Portfolio,
)

from risk.models.exposure_snapshot import (
    ExposureSnapshot,
)

from risk.models.position_size import (
    PositionSize,
)

from risk.models.risk_budget import (
    RiskBudget,
)

from strategies.framework.strategy_decision import (
    StrategyDecision,
)


@dataclass(
    frozen=True,
    slots=True,
)
class RiskContext:

    decision: StrategyDecision

    position_size: PositionSize

    portfolio: Portfolio

    available_capital: float

    exposure: ExposureSnapshot

    budget: RiskBudget