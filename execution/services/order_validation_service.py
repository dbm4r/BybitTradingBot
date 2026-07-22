from execution.models.execution_context import (
    ExecutionContext,
)

from risk.models.position_size import (
    PositionSize,
)

from risk.position_validator import (
    PositionValidator,
)


class OrderValidationService:

    @staticmethod
    def validate(
        engine,
        context: ExecutionContext,
    ) -> PositionSize:

        instrument = engine.exchange.get_instrument(
            engine.symbol,
        )

        quantity = instrument.round_quantity(
            context.position_size.quantity,
        )

        quantity = PositionValidator.validate(
            quantity=quantity,
            price=context.entry_price,
            available_cash=context.available_capital,
        )

        if not instrument.validate_quantity(
            quantity,
        ):
            raise RuntimeError(
                f"Invalid quantity: {quantity}"
            )

        return PositionSize(
            quantity=quantity,
            risk_amount=context.position_size.risk_amount,
            risk_percent=context.position_size.risk_percent,
            entry_price=context.position_size.entry_price,
            stop_price=context.position_size.stop_price,
        )