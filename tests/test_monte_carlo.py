from core.settings import Settings
from data.data_manager import DataManager
from strategies.framework.strategy_factory import StrategyFactory
from backtesting.backtester import Backtester
from validation.monte_carlo import MonteCarloValidator


settings = Settings()

manager = DataManager()

dataframe = manager.download_historical_data(
    symbol="BTCUSDT",
    interval="1",
    limit=5000,
)

strategy = StrategyFactory.create(
    "EMA",
)

backtester = Backtester(
    settings=settings,
    symbol="BTCUSDT",
    strategy=strategy,
)

trades = backtester.run(
    dataframe,
)



print(
    f"Generated {len(trades)} trades."
)

validator = MonteCarloValidator(
    iterations=1000,
)

validator.validate(
    trades=trades,
    initial_balance=backtester.portfolio.initial_balance,
)

validator.print_report()