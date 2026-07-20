from dataclasses import dataclass

from strategies.framework.base_strategy import BaseStrategy


@dataclass(slots=True, frozen=True)
class StrategyStage:
    """
    One executable stage inside the strategy pipeline.
    """

    strategy: BaseStrategy

    enabled: bool = True

    priority: int = 100