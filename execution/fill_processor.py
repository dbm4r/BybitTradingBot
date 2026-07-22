from backtesting.trade import (
    Trade,
)

from finance.trade_calculator import (
    TradeCalculator,
)

from orders.models.fill import (
    Fill,
)

from portfolio.portfolio_service import (
    PortfolioService,
)


class FillProcessor:

    @staticmethod
    def process_entry_fill(
        engine,
        context,
    ):

        order = context.order

        timestamp = (
            context.decision.candle.timestamp
        )

        fill = Fill(
            quantity=context.position_size.quantity,
            price=context.entry_price,
            timestamp=timestamp,
            fee=context.fee,
        )

        cash_after_fee = (
            context.available_capital
        )

        stop_price = (
            context.stop_price
        )

        take_profit_price = (
            context.take_profit_price
        )

        engine.order_manager.fill(
            engine=engine,
            order=order,
            fill=fill,
        )

        position = engine.portfolio.get_position(
            engine.symbol,
        )

        PortfolioService.open_position(
            portfolio=engine.portfolio,
            position=position,
            quantity=fill.quantity,
            price=fill.price,
            timestamp=fill.timestamp,
            cash_after_fee=cash_after_fee,
            stop_price=stop_price,
            take_profit_price=take_profit_price,
        )

        position_cost = (
            fill.quantity * fill.price
        )

        print("\n========== BUY ==========")
        print(f"Symbol        : {engine.symbol}")
        print(f"Quantity      : {fill.quantity:.6f}")
        print(f"Entry Price   : {fill.price:.2f}")
        print(f"Position Cost : {position_cost:.2f}")
        print(f"Cash Left     : {engine.portfolio.cash:.2f}")
        print(f"Stop Price    : {stop_price:.2f}")
        print(f"Take Profit   : {take_profit_price:.2f}")
        print("=========================\n")

    @staticmethod
    def process_exit_fill(
        engine,
        order,
        timestamp,
        price,
        exit_reason,
    ):

        fill = Fill(
            quantity=order.remaining_quantity,
            price=price,
            timestamp=timestamp,
        )

        engine.order_manager.fill(
            engine=engine,
            order=order,
            fill=fill,
        )

        position = engine.portfolio.get_position(
            engine.symbol,
        )

        gross_exit_value = TradeCalculator.exit_value(
            quantity=position.quantity,
            exit_price=fill.price,
        )

        fee = TradeCalculator.fee(
            value=gross_exit_value,
            fee_rate=engine.settings.trading_fee,
        )

        cash_received = TradeCalculator.cash_received(
            exit_value=gross_exit_value,
            fee=fee,
        )

        engine.total_fees += fee

        entry_value = TradeCalculator.entry_value(
            quantity=position.quantity,
            entry_price=position.entry_price,
        )

        gross_profit = TradeCalculator.gross_profit(
            entry_value=entry_value,
            exit_value=gross_exit_value,
        )

        net_profit = TradeCalculator.net_profit(
            gross_profit=gross_profit,
            fee=fee,
        )

        duration = (
            fill.timestamp - position.entry_time
        ).total_seconds() / 3600

        trade = Trade(
            symbol=engine.symbol,
            strategy=engine.strategy.name,
            entry_time=position.entry_time,
            exit_time=fill.timestamp,
            entry_price=position.entry_price,
            exit_price=fill.price,
            quantity=position.quantity,
            gross_profit=gross_profit,
            fees=fee,
            net_profit=net_profit,
            profit_percent=TradeCalculator.profit_percent(
                net_profit=net_profit,
                entry_value=entry_value,
            ),
            duration=duration,
            exit_reason=exit_reason,
        )

        engine.trades.append(
            trade,
        )

        print("\n========== SELL ==========")
        print(f"Symbol        : {engine.symbol}")
        print(f"Exit Price    : {fill.price:.2f}")
        print(f"Gross Profit  : {gross_profit:.2f}")
        print(f"Fees          : {fee:.2f}")
        print(f"Net Profit    : {net_profit:.2f}")
        print(f"Cash Received : {cash_received:.2f}")
        print("==========================\n")

        PortfolioService.close_position(
            portfolio=engine.portfolio,
            position=position,
            cash_received=cash_received,
        )