from market.regime_result import RegimeResult
from strategies.framework.base_strategy import BaseStrategy


class RegimeFilter:

    def allows(
        self,
        strategy: BaseStrategy,
        regime: RegimeResult,
    ) -> tuple[bool, str | None]:

        supported = strategy.supported_regimes

        if regime.trend not in supported["trend"]:
            return (
                False,
                f"{strategy.name} requires a trending market.",
            )

        if regime.volatility not in supported["volatility"]:
            return (
                False,
                f"{strategy.name} does not support the current volatility.",
            )

        if regime.liquidity not in supported["liquidity"]:
            return (
                False,
                f"{strategy.name} requires high liquidity.",
            )

        return (
            True,
            None,
        )