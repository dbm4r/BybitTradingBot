from market.regime_result import RegimeResult
from strategies.framework.strategy_decision import StrategyDecision


class RegimeFilter:

    def allows(
        self,
        decision: StrategyDecision,
        regime: RegimeResult,
    ) -> bool:

        return True