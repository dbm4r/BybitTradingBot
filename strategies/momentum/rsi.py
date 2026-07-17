from functools import cached_property
from market.market_regime import MarketRegime
from indicators.base_indicator import BaseIndicator
from indicators.rsi import RelativeStrengthIndex
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision


class RSIStrategy(BaseStrategy):

    def __init__(
        self,
        period: int = 14,
        oversold: float = 30,
        overbought: float = 70,
    ):

        if oversold >= overbought:
            raise ValueError(
                "Oversold must be smaller than overbought."
            )

        self.rsi = RelativeStrengthIndex(period)

        self.oversold = oversold
        self.overbought = overbought

    @property
    def name(self) -> str:
        return "RSI Strategy"

    @cached_property
    def parameters(self) -> dict:
        return {
            "period": self.rsi.period,
            "oversold": self.oversold,
            "overbought": self.overbought,
        }

    @property
    def indicators(
        self,
    ) -> tuple[BaseIndicator, ...]:

        return (
            self.rsi,
        )
    @property
    def supported_regimes(self) -> dict:

        return {
            "trend": [
                MarketRegime.RANGING,
            ],
            "volatility": [
                MarketRegime.LOW_VOLATILITY,
            ],
            "liquidity": [
                MarketRegime.HIGH_LIQUIDITY,
            ],
        }

    def evaluate(
        self,
        context: StrategyContext,
    ) -> StrategyDecision:

        result = context.get_indicator(
            self.rsi
        )

        if result is None:
            raise ValueError(
                "Required indicator is missing."
            )

        value = result.last

        candle = context.last_candle

        if value is None:
            return StrategyDecision(
                signal=SignalType.HOLD,
                confidence=1.0,
                reason="RSI is not ready.",
                strategy=self.name,
                candle=candle,
            )

        if value < self.oversold:
            return StrategyDecision(
                signal=SignalType.OPEN_LONG,
                confidence=1.0,
                reason="RSI entered oversold region.",
                strategy=self.name,
                candle=candle,
            )

        if value > self.overbought:
            return StrategyDecision(
                signal=SignalType.OPEN_SHORT,
                confidence=1.0,
                reason="RSI entered overbought region.",
                strategy=self.name,
                candle=candle,
            )

        return StrategyDecision(
            signal=SignalType.HOLD,
            confidence=1.0,
            reason="RSI is neutral.",
            strategy=self.name,
            candle=candle,
        )
    @property
    def requires_higher_timeframe_confirmation(
        self,
    ) -> bool:

        return False


    @property
    def confirmation_timeframes(
        self,
    ):

        return ()