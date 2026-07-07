from data.data_manager import DataManager
from strategies.sma_crossover import SMACrossoverStrategy
from backtesting.backtester import Backtester
from backtesting.trade_logger import TradeLogger
from core.settings import Settings
from risk.take_profit import TakeProfit
import backtesting.execution_engine

print(backtesting.execution_engine.__file__)

manager = DataManager()

df = manager.download_historical_data(
    symbol="BTCUSDT",
    interval="60",
    limit=500
)

strategy = SMACrossoverStrategy()

df = strategy.generate_signals(df)

settings = Settings()

backtester = Backtester(
    settings=settings,
    symbol="BTCUSDT",
    strategy_name="SMA Crossover"
)

trades = backtester.run(df)

backtester.print_report()
TradeLogger.export(
    trades,
    "results/trades.csv"
)
print(
    TakeProfit.percentage(
        60000,
        0.02
    )
)

print("Trades exported successfully.")
print(df.columns)
