from backtesting.trade import Trade
from risk.stop_loss import StopLoss
from risk.position_sizer import PositionSizer
from risk.position_validator import PositionValidator
from risk.risk_manager import RiskManager
from risk.take_profit import TakeProfit
from orders.order_manager import OrderManager
from orders.market_order import MarketOrder




class ExecutionEngine:

    def __init__(self, portfolio, settings, symbol, strategy_name):

        self.portfolio = portfolio
        self.settings = settings

        self.symbol = symbol
        self.strategy_name = strategy_name

        self.trades = []
        self.total_fees = 0
        self.risk_manager = RiskManager(self)
        self.order_manager = OrderManager()
    
    def buy(self, timestamp, price) -> None:

        order = MarketOrder(
            symbol=self.symbol,
            side="BUY",
            quantity=0,
            timestamp=timestamp
        )

        self.order_manager.submit(order)

        fee = self.portfolio.cash * self.settings.trading_fee

        cash_after_fee = self.portfolio.cash - fee

        self.total_fees += fee

        stop_price = StopLoss.percentage(
            entry_price=price,
            stop_percent=self.settings.stop_loss_percent
        )

        take_profit_price = TakeProfit.percentage(
            entry_price=price,
            take_profit_percent=self.settings.take_profit_percent
        )

        quantity = PositionSizer.fixed_risk(
            account_balance=cash_after_fee,
            risk_percent=self.settings.risk_per_trade,
            entry_price=price,
            stop_price=stop_price
        )
        quantity = PositionValidator.validate(
            quantity=quantity,
            price=price,
            available_cash=cash_after_fee
        )

        order.quantity = quantity

        self.order_manager.fill(
            order,
            price,
            timestamp
        )

        self.portfolio.position = quantity

        position_cost = quantity * price

        self.portfolio.cash = cash_after_fee - position_cost

        self.portfolio.entry_price = price
        self.portfolio.entry_time = timestamp
        self.portfolio.stop_price = stop_price
        self.portfolio.take_profit_price = take_profit_price
        self.portfolio.highest_price = price
        self.portfolio.break_even_active = False

        print("\n========== BUY ==========")
        print(f"Symbol        : {self.symbol}")
        print(f"Quantity      : {quantity:.6f}")
        print(f"Entry Price   : {price:.2f}")
        print(f"Position Cost : {position_cost:.2f}")
        print(f"Cash Left     : {self.portfolio.cash:.2f}")
        print(f"Stop Price        : {stop_price:.2f}")
        print(f"Take Profit Price : {take_profit_price:.2f}")
        print("=========================\n")
    def sell(self, timestamp, price, exit_reason) -> None:

        order = MarketOrder(
            symbol=self.symbol,
            side="SELL",
            quantity=self.portfolio.position,
            timestamp=timestamp
        )

        self.order_manager.submit(order)

        self.order_manager.fill(
            order,
            price,
            timestamp
        )


        gross_exit_value = self.portfolio.position * price

        fee = gross_exit_value * self.settings.trading_fee

        cash_received = gross_exit_value - fee

        self.total_fees += fee

        entry_value = (
            self.portfolio.position
            * self.portfolio.entry_price
        )

        gross_profit = gross_exit_value - entry_value

        net_profit = gross_profit - fee

        duration = (
            timestamp - self.portfolio.entry_time
        ).total_seconds() / 3600

        trade = Trade(
            symbol=self.symbol,
            strategy=self.strategy_name,

            entry_time=self.portfolio.entry_time,
            exit_time=timestamp,

            entry_price=self.portfolio.entry_price,
            exit_price=price,

            quantity=self.portfolio.position,

            gross_profit=gross_profit,
            fees=fee,
            net_profit=net_profit,

            profit_percent=(net_profit / entry_value) * 100,

            duration=duration,
            exit_reason=exit_reason
        )

        self.trades.append(trade)

        print("\n========== SELL ==========")
        print(f"Symbol        : {self.symbol}")
        print(f"Exit Price    : {price:.2f}")
        print(f"Gross Profit  : {gross_profit:.2f}")
        print(f"Fees          : {fee:.2f}")
        print(f"Net Profit    : {net_profit:.2f}")
        print(f"Cash Received : {cash_received:.2f}")
        print("==========================\n")

        self.portfolio.cash = cash_received

        self.portfolio.position = 0

        self.portfolio.entry_price = None
        self.portfolio.entry_time = None
        self.portfolio.stop_price = None
        self.portfolio.take_profit_price = None
        self.portfolio.highest_price = None
        self.portfolio.break_even_active = False
    def process_candle(self, row):

        # First check if an open trade should be closed by the stop loss
        self.risk_manager.process(row)

        signal = row["signal"]
        timestamp = row["timestamp"]
        price = row["close"]

        # Buy signal
        if signal == 1 and not self.portfolio.in_position():

            self.buy(timestamp, price)

        # Sell signal
        elif signal == -1 and self.portfolio.in_position():

            self.sell(
                timestamp,
                price,
                "Signal"
            )