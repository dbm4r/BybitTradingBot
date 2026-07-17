from runtime.cycle.trading_cycle import TradingCycle


print("========== TRADING CYCLE ==========\n")


class DummyScanner:

    def scan(
        self,
    ):

        print("Scanner")

        return [
            "BTCUSDT",
            "ETHUSDT",
        ]


class DummyPortfolio:

    def process(
        self,
        opportunities,
    ):

        print(
            "Portfolio",
            opportunities,
        )


class DummyExecution:

    def process(
        self,
    ):

        print(
            "Execution"
        )


cycle = TradingCycle(
    scanner=DummyScanner(),
    portfolio=DummyPortfolio(),
    execution=DummyExecution(),
)

cycle.run()