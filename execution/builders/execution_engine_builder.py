from backtesting.execution_engine import (
    ExecutionEngine,
)

from risk.builders.risk_engine_builder import (
    RiskEngineBuilder,
)

from risk.sizing.fixed_risk_sizer import (
    FixedRiskSizer,
)


class ExecutionEngineBuilder:

    def __init__(self):

        self._portfolio = None

        self._settings = None

        self._symbol = None

        self._strategy = None

        self._exchange_name = "BYBIT"

        self._position_sizer = (
            FixedRiskSizer()
        )

        self._risk_engine = (
            RiskEngineBuilder()
            .with_default_rules()
            .build()
        )

    def with_portfolio(
        self,
        portfolio,
    ):

        self._portfolio = portfolio

        return self

    def with_settings(
        self,
        settings,
    ):

        self._settings = settings

        return self

    def with_symbol(
        self,
        symbol,
    ):

        self._symbol = symbol

        return self

    def with_strategy(
        self,
        strategy,
    ):

        self._strategy = strategy

        return self

    def with_exchange(
        self,
        exchange_name,
    ):

        self._exchange_name = exchange_name

        return self

    def with_position_sizer(
        self,
        position_sizer,
    ):

        self._position_sizer = position_sizer

        return self

    def with_risk_engine(
        self,
        risk_engine,
    ):

        self._risk_engine = risk_engine

        return self

    def build(
        self,
    ):

        return ExecutionEngine(
            portfolio=self._portfolio,
            settings=self._settings,
            symbol=self._symbol,
            strategy=self._strategy,
            exchange_name=self._exchange_name,
            position_sizer=self._position_sizer,
            risk_engine=self._risk_engine,
        )