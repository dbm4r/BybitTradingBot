from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from models.candle import Candle
from pipeline.trading_pipeline import TradingPipeline
from strategies.framework.base_strategy import BaseStrategy
from strategies.framework.strategy_decision import StrategyDecision

if TYPE_CHECKING:
    from backtesting.execution_engine import (
        ExecutionEngine,
    )


@dataclass(slots=True)
class AssetContext:

    symbol: str

    strategy: BaseStrategy

    pipeline: TradingPipeline

    engine: ExecutionEngine

    latest_candle: Candle | None = None

    latest_decision: StrategyDecision | None = None

    enabled: bool = True

    metadata: dict[str, object] = field(
        default_factory=dict,
    )