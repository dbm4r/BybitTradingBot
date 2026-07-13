from abc import ABC, abstractmethod

from strategies.strategy_context import StrategyContext
from strategies.strategy_decision import StrategyDecision


class BaseStrategy(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Short strategy name.

        Examples:
            SMA Crossover
            EMA Crossover
            RSI Strategy
        """
        pass

    @property
    @abstractmethod
    def parameters(self) -> dict:
        """
        Strategy configuration.

        Example:
            {
                "fast_period": 20,
                "slow_period": 50,
            }
        """
        pass

    @abstractmethod
    def evaluate(
        self,
        context: StrategyContext,
    ) -> StrategyDecision:
        """
        Analyze the current market context and return
        a trading decision.
        """
        pass