from portfolio.asset_registry import AssetRegistry
from portfolio.portfolio_constraints import (
    PortfolioConstraints,
)
from portfolio.portfolio_guard import PortfolioGuard
from strategies.framework.signal_type import SignalType
from strategies.framework.strategy_decision import (
    StrategyDecision,
)
from models.candle import Candle
from datetime import datetime


guard = PortfolioGuard(
    PortfolioConstraints(
        max_open_positions=3,
    )
)

decision = StrategyDecision(
    signal=SignalType.OPEN_LONG,
    confidence=1.0,
    reason="Test",
    strategy="Test Strategy",
    candle=Candle(
        symbol="BTCUSDT",
        interval="1",
        timestamp=datetime.now(),
        open=100,
        high=101,
        low=99,
        close=100,
        volume=1000,
        turnover=100000,
    ),
)

allowed, reason = guard.allows(
    assets=AssetRegistry(),
    decision=decision,
)

print("========== PORTFOLIO GUARD ==========\n")

print("Allowed :", allowed)
print("Reason  :", reason)