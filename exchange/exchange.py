from abc import ABC, abstractmethod

class Exchange(ABC):

    @abstractmethod
    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
    ):
        pass

    @abstractmethod
    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
    ):
        pass

    @abstractmethod
    def cancel_order(
        self,
        order_id: str,
    ):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_positions(self):
        pass

    @abstractmethod
    def get_open_orders(self):
        pass