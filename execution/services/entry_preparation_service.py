from execution.models.execution_context import (
    ExecutionContext,
)

from finance.slippage_calculator import (
    SlippageCalculator,
)

from risk.stop_loss import (
    StopLoss,
)

from risk.take_profit import (
    TakeProfit,
)


class EntryPreparationService:

    @staticmethod
    def prepare(
        engine,
        decision,
    ) -> ExecutionContext:

        fee = (
            engine.portfolio.cash
            * engine.settings.trading_fee
        )

        available_capital = (
            engine.portfolio.cash
            - fee
        )

        entry_price = (
            SlippageCalculator.apply_buy(
                price=decision.candle.close,
                slippage_percent=(
                    engine.settings.slippage_percent
                ),
            )
        )

        stop_price = (
            StopLoss.percentage(
                entry_price=entry_price,
                stop_percent=(
                    engine.settings.stop_loss_percent
                ),
            )
        )

        take_profit_price = (
            TakeProfit.percentage(
                entry_price=entry_price,
                take_profit_percent=(
                    engine.settings.take_profit_percent
                ),
            )
        )

        position_size = (
            engine.position_sizer.calculate(
                available_capital=available_capital,
                risk_percent=(
                    engine.settings.risk_per_trade
                ),
                entry_price=entry_price,
                stop_price=stop_price,
            )
        )

        return ExecutionContext(
            decision=decision,
            portfolio=engine.portfolio.portfolio,
            available_capital=available_capital,
            position_size=position_size,
            entry_price=entry_price,
            stop_price=stop_price,
            take_profit_price=take_profit_price,
            fee=fee,
            slippage=(
                engine.settings.slippage_percent
            ),
        )