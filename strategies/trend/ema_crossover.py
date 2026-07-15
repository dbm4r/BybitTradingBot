from functools import cached_property
from market.market_regime import MarketRegime
from indicators.base_indicator import BaseIndicator
from indicators.ema import ExponentialMovingAverage
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_context import StrategyContext
from strategies.framework.strategy_decision import StrategyDecision


class EMACrossoverStrategy(BaseStrategy):

    def __init__(
        self,
        fast_period: int = 20,
        slow_period: int = 50,
    ):

        if fast_period >= slow_period:
            raise ValueError(
                "Fast period must be smaller than slow period."
            )

        self.fast_ema = ExponentialMovingAverage(
            fast_period
        )

        self.slow_ema = ExponentialMovingAverage(
            slow_period
        )

    @property
    def name(self) -> str:
        return "EMA Crossover"

    @cached_property
    def parameters(self) -> dict:
        return {
            "fast_period": self.fast_ema.period,
            "slow_period": self.slow_ema.period,
        }

    @property
    def indicators(
        self,
    ) -> tuple[BaseIndicator, ...]:

        return (
            self.fast_ema,
            self.slow_ema,
        )
    @property
    def supported_regimes(self) -> dict:

        return {
            "trend": [
                MarketRegime.TRENDING,
            ],
            "volatility": [
                MarketRegime.HIGH_VOLATILITY,
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

        fast = context.get_indicator(
            self.fast_ema
        )

        slow = context.get_indicator(
            self.slow_ema
        )

        if fast is None or slow is None:
            raise ValueError(
                "Required indicators are missing."
            )

        fast_value = fast.last
        slow_value = slow.last

        candle = context.last_candle

        if fast_value is None or slow_value is None:
            return StrategyDecision(
                signal=SignalType.HOLD,
                confidence=1.0,
                reason="Indicators are not ready.",
                strategy=self.name,
                candle=candle,
            )

        if fast_value > slow_value:
            return StrategyDecision(
                signal=SignalType.OPEN_LONG,
                confidence=1.0,
                reason="Fast EMA crossed above Slow EMA.",
                strategy=self.name,
                candle=candle,
            )

        if fast_value < slow_value:
            return StrategyDecision(
                signal=SignalType.OPEN_SHORT,
                confidence=1.0,
                reason="Fast EMA crossed below Slow EMA.",
                strategy=self.name,
                candle=candle,
            )

        return StrategyDecision(
            signal=SignalType.HOLD,
            confidence=1.0,
            reason="No crossover detected.",
            strategy=self.name,
            candle=candle,
        )