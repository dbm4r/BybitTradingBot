from backtesting.portfolio import Portfolio
from backtesting.execution_engine import ExecutionEngine
from backtesting.statistics import Statistics


class Backtester:

    def __init__(self, initial_balance=10000):

        self.portfolio = Portfolio(initial_balance)
        self.execution = ExecutionEngine(self.portfolio)

        self.trades = []

    def run(self, df):

        for _, row in df.iterrows():

            signal = row["signal"]
            price = row["close"]
            timestamp = row["timestamp"]

            self.execution.process_signal(
                signal=signal,
                timestamp=timestamp,
                price=price
            )

        # Close any remaining open position
        if self.portfolio.in_position():

            last_row = df.iloc[-1]

            self.execution.sell(
                timestamp=last_row["timestamp"],
                price=last_row["close"]
            )

        self.trades = self.execution.trades

        return self.trades

    def print_report(self):

        total_profit = Statistics.total_profit(self.trades)
        total_trades = Statistics.total_trades(self.trades)

        winners = Statistics.winning_trades(self.trades)
        losers = Statistics.losing_trades(self.trades)

        win_rate = Statistics.win_rate(self.trades)

        average_win = Statistics.average_win(self.trades)
        average_loss = Statistics.average_loss(self.trades)

        fees = self.execution.total_fees

        final_balance = self.portfolio.cash

        roi = (
            (final_balance - self.portfolio.initial_balance)
            / self.portfolio.initial_balance
        ) * 100

        print("\n========== BACKTEST REPORT ==========")

        print(f"Initial Balance : ${self.portfolio.initial_balance:,.2f}")
        print(f"Final Balance   : ${final_balance:,.2f}")

        print()

        print(f"Net Profit      : ${total_profit:,.2f}")
        print(f"Trading Fees   : ${fees:,.2f}")
        print(f"Return          : {roi:.2f}%")

        print()

        print(f"Trades          : {total_trades}")
        print(f"Winners         : {winners}")
        print(f"Losers          : {losers}")
        print(f"Win Rate        : {win_rate:.2f}%")

        print()

        print(f"Average Win     : ${average_win:.2f}")
        print(f"Average Loss    : ${average_loss:.2f}")

        print("=====================================\n")