from orders.market_order import MarketOrder
from risk.stop_loss import StopLoss
from risk.take_profit import TakeProfit
from risk.position_sizer import PositionSizer
from risk.position_validator import PositionValidator
from finance.slippage_calculator import SlippageCalculator
from execution.execution_coordinator import ExecutionCoordinator
from engine.engine_state import EngineState

class EntryExecutor:

    @staticmethod
    def execute(
        engine,
        timestamp,
        price,
    ):
        engine.state.set_state(
            EngineState.PLACING_ORDER
        )

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
            slippage_percent=engine.settings.slippage_percent,
        )

        stop_price = StopLoss.percentage(
            entry_price=price,
            stop_percent=engine.settings.stop_loss_percent,
        )

        take_profit_price = TakeProfit.percentage(
            entry_price=price,
            take_profit_percent=engine.settings.take_profit_percent,
        )

        quantity = PositionSizer.fixed_risk(
            available_capital=cash_after_fee,
            risk_percent=engine.settings.risk_per_trade,
            entry_price=price,
            stop_price=stop_price,
        )

        quantity = PositionValidator.validate(
            quantity=quantity,
            price=price,
            available_cash=cash_after_fee,
        )

        quantity = engine.exchange.instrument.round_quantity(
            quantity,
        )

        if not engine.exchange.instrument.validate_quantity(
            quantity,
        ):
            raise RuntimeError(
                f"Invalid quantity: {quantity}"
            )

        price = engine.exchange.instrument.round_price(
            price,
        )

        print("\n========== ORDER ==========")
        print(f"Price    : {price}")
        print(f"Quantity : {quantity}")
        print("===========================\n")

        order = MarketOrder(
            symbol=engine.symbol,
            side="BUY",
            quantity=quantity,
            timestamp=timestamp,
        )

        engine.order_manager.submit(
            engine,
            order,
        )

        result = engine.exchange.place_market_order(
            symbol=order.symbol,
            side=order.side,
            quantity=order.quantity,
        )

        if not result.success:
            raise RuntimeError(
                result.error
            )

        ExecutionCoordinator.process_entry(
            engine=engine,
            order=order,
            exchange_result=result,
            timestamp=timestamp,
            price=price,
            quantity=quantity,
            cash_after_fee=cash_after_fee,
            stop_price=stop_price,
            take_profit_price=take_profit_price,
        )

        engine.exchange.set_trading_stop(
            symbol=order.symbol,
            take_profit=take_profit_price,
            stop_loss=stop_price,
        )

        engine.state.set_state(
            EngineState.IN_POSITION
        )