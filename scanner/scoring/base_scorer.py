from abc import ABC, abstractmethod

from market.regime_result import RegimeResult


class BaseScorer(ABC):

    @abstractmethod
    def score(
        self,
        regime: RegimeResult,
    ) -> float:
        pass