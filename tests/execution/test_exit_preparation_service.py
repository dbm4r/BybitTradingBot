from execution.services.exit_preparation_service import (
    ExitPreparationService,
)

from backtesting.portfolio import (
    Portfolio,
)

from core.settings import (
    Settings,
)


class DummyPosition:

    quantity = 2.5


class DummyPortfolioManager:

    def __init__(self):

        self.portfolio = Portfolio(
            10000,
        )

        self.cash = 10000

    def get_position(
        self,
        symbol,
    ):

        return DummyPosition()


class DummyEngine:

    symbol = "BTCUSDT"

    settings = Settings()

    portfolio = DummyPortfolioManager()


def test_prepare_exit():

    context = (
        ExitPreparationService.prepare(
            engine=DummyEngine(),
            timestamp=None,
            price=100,
            exit_reason="Manual",
        )
    )

    assert (
        context.position_size.quantity
        == 2.5
    )

    assert (
        context.entry_price > 0
    )