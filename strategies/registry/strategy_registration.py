from dataclasses import dataclass

from strategies.framework.base_strategy import BaseStrategy
from strategies.registry.strategy_metadata import (
    StrategyMetadata,
)


@dataclass(slots=True, frozen=True)
class StrategyRegistration:
    """
    Associates strategy metadata with its implementation.
    """

    metadata: StrategyMetadata

    strategy: BaseStrategy