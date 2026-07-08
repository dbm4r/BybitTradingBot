from data.data_manager import DataManager

from strategies.strategy_factory import StrategyFactory

from backtesting.backtester import Backtester
from backtesting.comparison.comparison_runner import ComparisonRunner

from backtesting.performance.trade_logger import TradeLogger

from core.settings import Settings
from core.config import Config


def run_single_backtest(
    config,
    dataframe
):

    settings = Settings()

    strategy = StrategyFactory.create(
        config.strategy
    )

    dataframe = strategy.generate_signals(
        dataframe
    )

    backtester = Backtester(
        settings=settings,
        symbol=config.symbol,
        strategy=strategy
    )

    trades = backtester.run(
        dataframe
    )

    backtester.print_report()

    TradeLogger.export(
        trades,
        "results/trades.csv"
    )


def run_strategy_comparison(
    config,
    dataframe
):

    settings = Settings()

    strategies = [

        StrategyFactory.create("SMA"),

        StrategyFactory.create("EMA"),

        StrategyFactory.create("RSI")

    ]

    runner = ComparisonRunner(
        settings=settings,
        symbol=config.symbol
    )

    runner.compare(
        dataframe=dataframe,
        strategies=strategies
    )

    runner.print_report()


def main():

    config = Config()

    manager = DataManager()

    dataframe = manager.download_historical_data(
        symbol=config.symbol,
        interval=config.interval,
        limit=config.limit
    )

    if config.mode == "single":

        run_single_backtest(
            config,
            dataframe.copy()
        )

    elif config.mode == "comparison":

        run_strategy_comparison(
            config,
            dataframe.copy()
        )

    else:

        raise ValueError(
            f"Unknown mode: {config.mode}"
        )


if __name__ == "__main__":

    main()