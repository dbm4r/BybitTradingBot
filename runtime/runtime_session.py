from dataclasses import dataclass, field
from datetime import datetime

from runtime.runtime_state import RuntimeState


@dataclass(slots=True)
class RuntimeSession:

    state: RuntimeState = RuntimeState.STOPPED

    started_at: datetime | None = None

    stopped_at: datetime | None = None

    reconnect_count: int = 0

    healthy: bool = True

    metadata: dict = field(
        default_factory=dict,
    )