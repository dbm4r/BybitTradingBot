from abc import ABC, abstractmethod

from risk.models.position_size import (
    PositionSize,
)


class BasePositionSizer(
    ABC,
):

    @property
    @abstractmethod
    def name(
        self,
    ) -> str:
        ...

    @abstractmethod
    def calculate(
        self,
        available_capital: float,
        risk_percent: float,
        entry_price: float,
        stop_price: float,
    ) -> PositionSize:
        ...