from core.config import Config
from data.data_manager import DataManager
from market.candle_factory import CandleFactory
from portfolio.portfolio_manager import PortfolioManager
from strategies.trend.sma_crossover import SMACrossoverStrategy


config = Config()

manager = PortfolioManager()

symbols = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
]

for symbol in symbols:

    manager.register_asset(
        symbol=symbol,
        strategy=SMACrossoverStrategy(
            fast_period=5,
            slow_period=20,
        ),
    )

print("========== PORTFOLIO PROCESSING ==========\n")

for symbol in symbols:

    dataframe = DataManager().download_historical_data(
        symbol=symbol,
        interval="1",
        limit=50,
    )

    for _, row in dataframe.iterrows():

        candle = CandleFactory.from_series(
            row=row,
            symbol=symbol,
            interval="1",
        )

        decision = manager.process_candle(
            candle
        )
        asset = manager.get_asset(
            symbol
        )

        allocation = asset.metadata[
            "capital_allocation"
        ]

    print(
        f"{symbol:<10} -> "
        f"{decision.signal.name:<12} "
        f"${allocation:,.2f}"
    )