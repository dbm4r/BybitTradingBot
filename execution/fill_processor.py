from portfolio.portfolio_service import PortfolioService
from backtesting.trade import Trade
from finance.trade_calculator import TradeCalculator

class FillProcessor:

    @staticmethod
    def process_entry_fill(
        engine,
        order,
        timestamp,
        price,
        quantity,
        cash_after_fee,
        stop_price,
        take_profit_price
    ):

        engine.order_manager.fill(
            engine,
            order,
            quantity,
            price,
            timestamp
        )

        position = engine.portfolio.get_position(
            engine.symbol
        )

        PortfolioService.open_position(
            portfolio=engine.portfolio,
            position=position,
            quantity=quantity,
            price=price,
            timestamp=timestamp,
            cash_after_fee=cash_after_fee,
            stop_price=stop_price,
            take_profit_price=take_profit_price
        )

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

    @staticmethod
    def process_exit_fill(
        engine,
        order,
        timestamp,
        price,
        exit_reason
    ):

        engine.order_manager.fill(
            engine,
            order,
            order.remaining_quantity,
            price,
            timestamp
        )

        position = engine.portfolio.get_position(
            engine.symbol
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
            timestamp - position.entry_time
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
                entry_value=entry_value
            ),
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