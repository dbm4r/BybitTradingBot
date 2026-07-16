from portfolio.asset_registry import AssetRegistry
from portfolio.exposure_manager import ExposureManager
from portfolio.portfolio_constraints import (
    PortfolioConstraints,
)
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)


class PortfolioGuard:

    def __init__(
        self,
        constraints: PortfolioConstraints,
    ):

        self.constraints = constraints

    def allows(
        self,
        assets: AssetRegistry,
        decision: StrategyDecision,
    ) -> tuple[bool, str | None]:

        if decision.signal != SignalType.OPEN_LONG:
            return True, None

        if ExposureManager.has_open_position(
            assets,
            decision.candle.symbol,
        ):
            return (
                False,
                "Position already open.",
            )

        if (
            ExposureManager.open_positions(
                assets
            )
            >= self.constraints.max_open_positions
        ):
            return (
                False,
                "Maximum open positions reached.",
            )

        return True, None