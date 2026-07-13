from abc import ABC, abstractmethod

from indicators.base_indicator import BaseIndicator
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision


class BaseStrategy(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Strategy name.
        """
        pass

    @property
    @abstractmethod
    def parameters(self) -> dict:
        """
        Strategy configuration.
        """
        pass

    @property
    @abstractmethod
    def indicators(self) -> tuple[BaseIndicator, ...]:
        """
        Indicators required by this strategy.
        """
        pass

    @abstractmethod
    def evaluate(
        self,
        context: StrategyContext,
    ) -> StrategyDecision:
        """
        Analyze the market and return a trading decision.
        """
        pass