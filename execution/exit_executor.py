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
        position = engine.portfolio.get_position(
            engine.symbol
        )
        price = SlippageCalculator.apply_sell(
            price=price,
            slippage_percent=engine.settings.slippage_percent
        )

        order = MarketOrder(
            symbol=engine.symbol,
            side="SELL",
            quantity=position.quantity,
            timestamp=timestamp
        )

        engine.order_manager.submit(
            engine,
            order
        )
        result = engine.exchange.place_market_order(
            symbol=order.symbol,
            side=order.side,
            quantity=order.quantity
        )

        if not result.success:
            raise RuntimeError(result.error)

        exchange_order = result.order

        engine.order_manager.fill(
            engine,
            order,
            order.remaining_quantity,
            price,
            timestamp
        )

        gross_exit_value = TradeCalculator.exit_value(
            quantity=position.quantity,
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
            quantity=position.quantity,
            entry_price=position.entry_price
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
            - position.entry_time
        ).total_seconds() / 3600

        trade = Trade(
            symbol=engine.symbol,
            strategy=engine.strategy.name,

            entry_time=position.entry_time,
            exit_time=timestamp,

            entry_price=position.entry_price,
            exit_price=price,

            quantity=position.quantity,

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

        PortfolioService.close_position(
            portfolio=engine.portfolio,
            position=position,
            cash_received=cash_received
        )