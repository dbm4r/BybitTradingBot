from config import (
    BYBIT_API_KEY,
    BYBIT_API_SECRET,
)
from exchange.bybit_exchange import BybitExchange
from exchange.paper_exchange import PaperExchange
from runtime.trading_runtime_builder import TradingRuntimeBuilder
from strategies.trend.sma_crossover import SMACrossover


def main():

    paper_exchange = PaperExchange(
        symbol="BTCUSDT",
    )

    market_data = BybitExchange(
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    )

    runtime = (
        TradingRuntimeBuilder()
        .exchange(
            paper_exchange
        )
        .market_data(
            market_data
        )
        .strategy(
            SMACrossover()
        )
        .symbols(
            [
                "BTCUSDT",
            ]
        )
        .build()
    )

    runtime.run()


if __name__ == "__main__":
    main()