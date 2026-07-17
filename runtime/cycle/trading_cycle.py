from runtime.cycle.trading_context import TradingContext


class TradingCycle:

    def __init__(
        self,
        context: TradingContext,
    ):

        self.context = context

    def pre_cycle(
        self,
    ) -> None:

        """
        Prepare the trading cycle.

        Future:
        - Synchronize exchange
        - Refresh balances
        - Refresh positions
        - Update market state
        """

        pass

    def scan(
        self,
    ):
        """
        Scan the market and return opportunities.
        """

        return self.context.scanner.scan()

    def process(
        self,
        opportunities,
    ) -> None:
        """
        Process opportunities through the portfolio.
        """

        self.context.processor.process(
            opportunities
        )

    def post_cycle(
        self,
    ) -> None:

        """
        Finish the trading cycle.

        Future:
        - Statistics
        - Performance metrics
        - Logging
        - Reporting
        - Event publishing
        """

        pass

    def run(
        self,
    ) -> None:

        self.pre_cycle()

        opportunities = self.scan()

        self.process(
            opportunities
        )

        self.post_cycle()