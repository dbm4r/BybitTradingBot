from data.data_manager import DataManager
from strategies.sma_crossover import SMACrossoverStrategy
from backtesting.backtester import Backtester
from backtesting.trade_logger import TradeLogger

manager = DataManager()

df = manager.download_historical_data(
    symbol="BTCUSDT",
    interval="60",
    limit=500
)

strategy = SMACrossoverStrategy()

df = strategy.generate_signals(df)

backtester = Backtester()

trades = backtester.run(df)

backtester.print_report()
TradeLogger.export(
    trades,
    "results/trades.csv"
)

print("Trades exported successfully.")
