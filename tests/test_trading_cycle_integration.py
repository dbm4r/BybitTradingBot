from runtime.cycle.trading_context import TradingContext
from runtime.cycle.trading_cycle import TradingCycle
from runtime.cycle.opportunity_processor import OpportunityProcessor


print("========== TRADING CYCLE INTEGRATION ==========\n")


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
            DummyOpportunity("BTCUSDT"),
            DummyOpportunity("ETHUSDT"),
        ]


class DummySeries:

    @property
    def last(
        self,
    ):

        return "Latest Candle"


class DummyMarketLoader:

    def load(
        self,
        symbol,
        interval,
        limit,
    ):

        print(
            f"Loading candles for {symbol}"
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
            f"Portfolio processing {candle}"
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
            f"Execution ({engine}, {decision})"
        )


processor = OpportunityProcessor(
    portfolio=DummyPortfolio(),
    execution=DummyExecution(),
    market_loader=DummyMarketLoader(),
)

context = TradingContext(
    scanner=DummyScanner(),
    processor=processor,
)

cycle = TradingCycle(
    context=context,
)

cycle.run()