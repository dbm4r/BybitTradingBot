from risk.risk_manager import RiskManager
from orders.order_manager import OrderManager
from execution.entry_executor import EntryExecutor
from execution.exit_executor import ExitExecutor
from events.event_bus import EventBus
from events.event_names import EventNames
from exchange.exchange_factory import ExchangeFactory
from execution.execution_state import ExecutionState
from execution.execution_listener import ExecutionListener
from exchange.exchange_synchronizer import (
    ExchangeSynchronizer
)
from engine.state_manager import StateManager
from exchange.instrument_service import InstrumentService
from strategies.framework.signal_type import SignalType



class ExecutionEngine:

    def __init__(self, portfolio, settings, symbol, strategy, exchange_name="BYBIT"):
        self.portfolio = portfolio
        self.settings = settings
        self.exchange = ExchangeFactory.create(
            exchange_name,
            settings,
            symbol,
        )
        

        self.symbol = symbol
        self.strategy = strategy

        self.trades = []
        self.total_fees = 0
        self.risk_manager = RiskManager(self)
        self.events = EventBus()
        self.order_manager = OrderManager()
        self.execution_state = ExecutionState()
        self.state = StateManager()
        self.execution_listener = ExecutionListener(
            self
        )
        self.synchronizer = ExchangeSynchronizer(
            self
        )
        self.events.subscribe(
            EventNames.ORDER_SUBMITTED,
            lambda order: print(
                f"[EVENT] Order Submitted: {order.side}"
            )
        )
        self.events.subscribe(
            EventNames.ORDER_FILLED,
            lambda order: print(
                f"[EVENT] Order Filled: "
                f"{order.side} "
                f"{order.filled_quantity:.6f}"
            )
        )
        
    
    def buy(self, timestamp, price) -> None:

        EntryExecutor.execute(
            engine=self,
            timestamp=timestamp,
            price=price)

    def sell(
            self, timestamp, price, exit_reason) -> None:

        ExitExecutor.execute(
            engine=self,
            timestamp=timestamp,
            price=price,
            exit_reason=exit_reason
        )
    def process_candle(self, row):
        """
        Legacy compatibility layer.

        Scheduled for removal after all
        DataFrame-based execution has been
        migrated to TradingSession.
        """

        self.risk_manager.process(row)

        signal = row["signal"]
        timestamp = row["timestamp"]
        price = row["close"]

        position = self.portfolio.get_position(
            self.symbol
        )

        if signal == 1 and not position.is_open():

            self.buy(timestamp, price)

        elif signal == -1 and position.is_open():

            self.sell(
                timestamp,
                price,
                "Signal"
            )
    


    def process_decision(
        self,
        decision,
    ) -> None:

        position = self.portfolio.get_position(
            self.symbol
        )

        candle = decision.candle

        match decision.signal:

            case SignalType.OPEN_LONG:

                if not position.is_open():

                    self.buy(
                        timestamp=candle.timestamp,
                        price=candle.close,
                    )

            case SignalType.OPEN_SHORT:

                if position.is_open():

                    self.sell(
                        timestamp=candle.timestamp,
                        price=candle.close,
                        exit_reason=decision.reason,
                    )

            case SignalType.HOLD:
                return

            case _:
                raise ValueError(
                    f"Unsupported signal: {decision.signal}"
                )