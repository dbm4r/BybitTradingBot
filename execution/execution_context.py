from dataclasses import dataclass

from exchange.base_exchange import BaseExchange
from portfolio.portfolio import Portfolio
from orders.order_manager import OrderManager
from instruments.instrument import Instrument
from strategies.framework.base_strategy import BaseStrategy
from engine.engine_state_manager import EngineStateManager
from settings.engine_settings import EngineSettings


@dataclass(slots=True)
class ExecutionContext:

    exchange: BaseExchange

    portfolio: Portfolio

    order_manager: OrderManager

    instrument: Instrument

    settings: EngineSettings

    state: EngineStateManager

    strategy: BaseStrategy

    symbol: str

    total_fees: float = 0.0