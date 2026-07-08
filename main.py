from data.data_manager import DataManager
from strategies.strategy_factory import StrategyFactory
from backtesting.backtester import Backtester
from backtesting.performance.trade_logger import TradeLogger
from core.settings import Settings
from core.config import Config



def main():

    config = Config()

    manager = DataManager()

    df = manager.download_historical_data(
        symbol=config.symbol,
        interval=config.interval,
        limit=config.limit
    )

    strategy = StrategyFactory.create(
        config.strategy
        )
    df = strategy.generate_signals(df)

    settings = Settings()

    

    backtester = Backtester(
        settings=settings,
        symbol=config.symbol,
        strategy=strategy
    )

    trades = backtester.run(df)

    backtester.print_report()

    TradeLogger.export(
        trades,
        "results/trades.csv",
       
    )


if __name__ == "__main__":
    main()