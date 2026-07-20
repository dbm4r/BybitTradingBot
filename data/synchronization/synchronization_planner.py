from datetime import timedelta

from data.models.download_request import DownloadRequest
from data.synchronization.synchronization_plan import (
    SynchronizationPlan,
)
from data.synchronization.synchronization_state import (
    SynchronizationState,
)


class SynchronizationPlanner:

    @staticmethod
    def plan(
        request: DownloadRequest,
        state: SynchronizationState,
    ) -> SynchronizationPlan:

        if not state.exists:

            return SynchronizationPlan(
                download_required=True,
                start=request.start,
                end=request.end,
            )

        if state.last_timestamp is None:

            return SynchronizationPlan(
                download_required=True,
                start=request.start,
                end=request.end,
            )

        if state.last_timestamp >= request.end:

            return SynchronizationPlan(
                download_required=False,
                start=None,
                end=None,
            )

        return SynchronizationPlan(
            download_required=True,
            start=state.last_timestamp + timedelta(
                milliseconds=1
            ),
            end=request.end,
        )