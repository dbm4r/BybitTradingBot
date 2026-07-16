from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)


class DecisionProcessor:

    @staticmethod
    def process(
        engine,
        decision: StrategyDecision,
    ) -> None:

        position = engine.portfolio.get_position(
            engine.symbol
        )

        signal = decision.signal

        candle = decision.candle

        match signal:

            case SignalType.OPEN_LONG:

                if not position.is_open():

                    engine.open_position(
                        timestamp=candle.timestamp,
                        price=candle.close,
                    )

            case SignalType.OPEN_SHORT:

                if position.is_open():

                    engine.close_position(
                        timestamp=candle.timestamp,
                        price=candle.close,
                        exit_reason=decision.reason,
                    )

            case SignalType.HOLD:

                return

            case _:

                raise ValueError(
                    f"Unsupported signal: {signal}"
                )