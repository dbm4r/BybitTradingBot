from execution.models.execution_context import (
    ExecutionContext,
)

from finance.slippage_calculator import (
    SlippageCalculator,
)

from risk.models.position_size import (
    PositionSize,
)


class ExitPreparationService:

    @staticmethod
    def prepare(
        engine,
        timestamp,
        price,
        exit_reason,
    ) -> ExecutionContext:

        position = engine.portfolio.get_position(
            engine.symbol,
        )

        exit_price = (
            SlippageCalculator.apply_sell(
                price=price,
                slippage_percent=(
                    engine.settings.slippage_percent
                ),
            )
        )

        return ExecutionContext(
            decision=None,
            portfolio=engine.portfolio.portfolio,
            available_capital=engine.portfolio.cash,
            position_size=PositionSize(
                quantity=position.quantity,
                risk_amount=0.0,
                risk_percent=0.0,
                entry_price=exit_price,
                stop_price=exit_price,
            ),
            entry_price=exit_price,
            stop_price=exit_price,
            take_profit_price=exit_price,
            fee=0.0,
            slippage=(
                engine.settings.slippage_percent
            ),
        )