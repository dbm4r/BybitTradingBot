from pipeline.trading_pipeline import TradingPipeline
from portfolio.asset_context import AssetContext
from portfolio.asset_registry import AssetRegistry
from strategies.framework.base_strategy import BaseStrategy
from models.candle import Candle
from strategies.framework.strategy_decision import (
    StrategyDecision,
)
from portfolio.capital_allocator import CapitalAllocator
from portfolio.portfolio_constraints import PortfolioConstraints
from portfolio.portfolio_guard import PortfolioGuard
from backtesting.execution_manager import ExecutionManager
from backtesting.portfolio import Portfolio
from core.settings import Settings
class PortfolioManager:

    def __init__(self):

        self.settings = Settings()

        self.portfolio = Portfolio(
            self.settings.initial_balance
        )

        self.execution = ExecutionManager(
            portfolio=self.portfolio,
            settings=self.settings,
        )

        self.assets = AssetRegistry()

        self.constraints = PortfolioConstraints()

        self.guard = PortfolioGuard(
            self.constraints
        )

        self.allocator = CapitalAllocator(
            self.constraints
        )

    def register_asset(
        self,
        symbol: str,
        strategy: BaseStrategy,
        interval: str = "1",
    ) -> None:

        if self.assets.exists(symbol):
            raise ValueError(
                f"{symbol} already registered."
            )

        pipeline = TradingPipeline(
            strategy=strategy,
            symbol=symbol,
            interval=interval,
        )

        engine = self.execution.get_engine(
            symbol=symbol,
            strategy=strategy,
        )

        asset = AssetContext(
            symbol=symbol,
            strategy=strategy,
            pipeline=pipeline,
            engine=engine,
        )


        self.assets.add(asset)

    def get_asset(
        self,
        symbol: str,
    ) -> AssetContext:

        return self.assets.get(symbol)

    def remove_asset(
        self,
        symbol: str,
    ) -> None:

        

        self.assets.remove(symbol)

    @property
    def symbols(
        self,
    ) -> tuple[str, ...]:

        return self.assets.symbols

    @property
    def count(
        self,
    ) -> int:

        return self.assets.count
    def process_candle(
        self,
        candle: Candle,
    ) -> StrategyDecision:

        asset = self.get_asset(
            candle.symbol
        )

        decision = asset.pipeline.process_candle(
            candle
        )

        asset.latest_candle = candle

        asset.latest_decision = decision

        allowed, reason = self.guard.allows(
            assets=self.assets,
            decision=decision,
        )

        if not allowed:

            return StrategyDecision.hold(
                candle=candle,
                strategy=decision.strategy,
                reason=reason,
            )

        allocation = self.allocator.allocate(
            self.portfolio,
        )

        asset.metadata["capital_allocation"] = allocation

        return decision
    def process_market(
        self,
        candles: list[Candle],
    ) -> list[StrategyDecision]:

        decisions = []

        for candle in candles:

            decisions.append(
                self.process_candle(
                    candle
                )
            )

        return decisions