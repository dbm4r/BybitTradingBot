from backtesting.trade import Trade
from orders.market_order import MarketOrder
from portfolio.portfolio_service import PortfolioService
from finance.trade_calculator import TradeCalculator
from finance.slippage_calculator import SlippageCalculator

class ExitExecutor:

    @staticmethod
    def execute(
        engine,
        timestamp,
        price,
        exit_reason
    ):
        price = SlippageCalculator.apply_sell(
            price=price,
            slippage_percent=engine.settings.slippage_percent
        )

        order = MarketOrder(
            symbol=engine.symbol,
            side="SELL",
            quantity=engine.portfolio.position,
            timestamp=timestamp
        )

        engine.order_manager.submit(order)

        engine.order_manager.fill(
            order,
            order.remaining_quantity,
            price,
            timestamp
        )

        gross_exit_value = TradeCalculator.exit_value(
            quantity=engine.portfolio.position,
            exit_price=price
        )

        fee = TradeCalculator.fee(
            value=gross_exit_value,
            fee_rate=engine.settings.trading_fee
        )

        cash_received = TradeCalculator.cash_received(
            exit_value=gross_exit_value,
            fee=fee
        )

        engine.total_fees += fee

        entry_value = TradeCalculator.entry_value(
            quantity=engine.portfolio.position,
            entry_price=engine.portfolio.entry_price
        )

        gross_profit = TradeCalculator.gross_profit(
            entry_value=entry_value,
            exit_value=gross_exit_value
        )

        net_profit = TradeCalculator.net_profit(
            gross_profit=gross_profit,
            fee=fee
        )

        duration = (
            timestamp
            - engine.portfolio.entry_time
        ).total_seconds() / 3600

        trade = Trade(
            symbol=engine.symbol,
            strategy=engine.strategy_name,

            entry_time=engine.portfolio.entry_time,
            exit_time=timestamp,

            entry_price=engine.portfolio.entry_price,
            exit_price=price,

            quantity=engine.portfolio.position,

            gross_profit=gross_profit,
            fees=fee,
            net_profit=net_profit,

            profit_percent=TradeCalculator.profit_percent(
            net_profit=net_profit,
            entry_value=entry_value),
            duration=duration,
            exit_reason=exit_reason
        )

        engine.trades.append(trade)

        print("\n========== SELL ==========")
        print(f"Symbol        : {engine.symbol}")
        print(f"Exit Price    : {price:.2f}")
        print(f"Gross Profit  : {gross_profit:.2f}")
        print(f"Fees          : {fee:.2f}")
        print(f"Net Profit    : {net_profit:.2f}")
        print(f"Cash Received : {cash_received:.2f}")
        print("==========================\n")

        PortfolioService.close_position(portfolio=engine.portfolio, cash_received=cash_received)