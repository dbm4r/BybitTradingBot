from dataclasses import dataclass

from market.timeframe_context import TimeframeContext


@dataclass(slots=True)
class MultiTimeframeContext:

    contexts: dict[str, TimeframeContext]

    def get(
        self,
        timeframe: str,
    ) -> TimeframeContext:

        return self.contexts[timeframe]