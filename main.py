from data.data_manager import DataManager
from strategies.framework.strategy_factory import StrategyFactory
from backtesting.backtester import Backtester
from backtesting.comparison.comparison_runner import ComparisonRunner
from backtesting.performance.trade_logger import TradeLogger
from core.settings import Settings
from core.config import Config
from optimization.optimizer import Optimizer
from optimization.parameter_grid import ParameterGrid
from validation.walk_forward import WalkForwardValidator
from validation.walk_forward_logger import WalkForwardLogger
from validation.monte_carlo import MonteCarloValidator
from validation.monte_carlo_logger import MonteCarloLogger

def run_single_backtest(
    config,
    dataframe
):

    settings = Settings()

    strategy = StrategyFactory.create(
        config.strategy
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

def run_optimization(
    config,
    dataframe
):

    settings = Settings()

    optimizer = Optimizer(
        settings=settings,
        symbol=config.symbol
    )

    grid = ParameterGrid(

        fast_period=[10, 20, 30],

        slow_period=[50, 100]

    )

    optimizer.optimize(
        dataframe=dataframe,
        strategy_name=config.strategy,
        parameter_grid=grid
    )

    optimizer.print_report()

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

def run_walk_forward(
    config,
    dataframe,
):

    settings = Settings()

    validator = WalkForwardValidator(
        settings=settings,
        symbol=config.symbol,
    )

    grid = ParameterGrid(

        fast_period=[10, 20, 30],

        slow_period=[50, 100]

    )

    results = validator.validate(
        dataframe=dataframe,
        strategy_name=config.strategy,
        parameter_grid=grid,
        train_size=300,
        test_size=100,
    )

    validator.print_report()

    WalkForwardLogger.export(
        results,
        "results/walk_forward.csv",
    )
def run_monte_carlo(
    config,
    dataframe,
):

    settings = Settings()

    strategy = StrategyFactory.create(
        config.strategy
    )

    backtester = Backtester(
        settings=settings,
        symbol=config.symbol,
        strategy=strategy,
    )

    trades = backtester.run(
        dataframe.copy()
    )

    validator = MonteCarloValidator(
        iterations=1000,
    )

    results = validator.validate(
        trades=trades,
        initial_balance=backtester.portfolio.initial_balance,
    )

    validator.print_report()

    MonteCarloLogger.export(
        results,
        "results/monte_carlo.csv",
    )
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

    elif config.mode == "optimization":

        run_optimization(
            config,
            dataframe.copy()
        )
    elif config.mode == "walk_forward":

        run_walk_forward(
            config,
            dataframe.copy(),
        )
    elif config.mode == "monte_carlo":

        run_monte_carlo(
            config,
            dataframe.copy(),
        )

    else:

        raise ValueError(
            f"Unknown mode: {config.mode}"
        )


if __name__ == "__main__":

    main()