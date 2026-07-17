from runtime.trading_runtime_builder import (
    TradingRuntimeBuilder,
)
from runtime.cycle.opportunity_processor import (
    OpportunityProcessor,
)


print("========== TRADING RUNTIME BUILDER ==========\n")


class DummyOpportunity:

    def __init__(
        self,
        symbol,
    ):

        self.symbol = type(
            "Symbol",
            (),
            {
                "symbol": symbol,
            },
        )()


class DummyScanner:

    def scan(
        self,
    ):

        print("Scanner")

        return [
            DummyOpportunity(
                "BTCUSDT"
            )
        ]


class DummySeries:

    @property
    def last(
        self,
    ):

        return "Latest Candle"


class DummyLoader:

    def load(
        self,
        symbol,
        interval,
        limit,
    ):

        print(
            f"Loading {symbol}"
        )

        return DummySeries()


class DummyAsset:

    def __init__(
        self,
    ):

        self.engine = "ENGINE"


class DummyPortfolio:

    def process_candle(
        self,
        candle,
    ):

        print(
            f"Portfolio {candle}"
        )

        return "DECISION"

    def get_asset(
        self,
        symbol,
    ):

        return DummyAsset()


class DummyExecution:

    def execute(
        self,
        engine,
        decision,
    ):

        print(
            f"Execution {decision}"
        )


processor = OpportunityProcessor(
    portfolio=DummyPortfolio(),
    execution=DummyExecution(),
    market_loader=DummyLoader(),
)

cycle = (
    TradingRuntimeBuilder()
    .scanner(
        DummyScanner()
    )
    .processor(
        processor
    )
    .build()
)

cycle.run()