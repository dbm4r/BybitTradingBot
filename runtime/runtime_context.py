from dataclasses import dataclass
from runtime.runtime_loop import RuntimeLoop
from runtime.runtime_scheduler import RuntimeScheduler
from runtime.runtime_lifecycle import RuntimeLifecycle
from runtime.runtime_session import RuntimeSession
from runtime.runtime_settings import RuntimeSettings


@dataclass(slots=True)
class RuntimeContext:

    session: RuntimeSession

    lifecycle: RuntimeLifecycle

    settings: RuntimeSettings

    trading_engine: object | None = None

    market_scanner: object | None = None

    portfolio_manager: object | None = None

    execution_coordinator: object | None = None

    exchange: object | None = None

    scheduler: object | None = None
    scheduler: RuntimeScheduler | None = None

    loop: RuntimeLoop | None = None