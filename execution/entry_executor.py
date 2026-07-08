from orders.market_order import MarketOrder
from risk.stop_loss import StopLoss
from risk.take_profit import TakeProfit
from risk.position_sizer import PositionSizer
from risk.position_validator import PositionValidator
from portfolio.portfolio_service import PortfolioService
from finance.slippage_calculator import SlippageCalculator


class EntryExecutor:

    @staticmethod
    def execute(
        engine,
        timestamp,
        price
    ):

        order = MarketOrder(
            symbol=engine.symbol,
            side="BUY",
            quantity=0,
            timestamp=timestamp
        )

        engine.order_manager.submit(order)

        fee = (
            engine.portfolio.cash
            * engine.settings.trading_fee
        )

        cash_after_fee = (
            engine.portfolio.cash - fee
        )

        engine.total_fees += fee
        price = SlippageCalculator.apply_buy(
            price=price,
            slippage_percent=engine.settings.slippage_percent
        )

        stop_price = StopLoss.percentage(
            entry_price=price,
            stop_percent=engine.settings.stop_loss_percent
        )

        take_profit_price = TakeProfit.percentage(
            entry_price=price,
            take_profit_percent=engine.settings.take_profit_percent
        )

        quantity = PositionSizer.fixed_risk(
            account_balance=cash_after_fee,
            risk_percent=engine.settings.risk_per_trade,
            entry_price=price,
            stop_price=stop_price
        )

        quantity = PositionValidator.validate(
            quantity=quantity,
            price=price,
            available_cash=cash_after_fee
        )

        order.quantity = quantity

        engine.order_manager.fill(
            order,
            order.remaining_quantity,
            price,
            timestamp
        )

        PortfolioService.open_position(
            portfolio=engine.portfolio,
            quantity=quantity,
            price=price,
            timestamp=timestamp,
            cash_after_fee=cash_after_fee,
            stop_price=stop_price,
            take_profit_price=take_profit_price)
        
        position_cost = quantity * price

        print("\n========== BUY ==========")
        print(f"Symbol        : {engine.symbol}")
        print(f"Quantity      : {quantity:.6f}")
        print(f"Entry Price   : {price:.2f}")
        print(f"Position Cost : {position_cost:.2f}")
        print(f"Cash Left     : {engine.portfolio.cash:.2f}")
        print(f"Stop Price    : {stop_price:.2f}")
        print(f"Take Profit   : {take_profit_price:.2f}")
        print("=========================\n")
        return