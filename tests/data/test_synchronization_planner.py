from datetime import datetime, timezone

from data.synchronization.synchronization_planner import (
    SynchronizationPlanner,
)
from data.synchronization.synchronization_state import (
    SynchronizationState,
)
from data.models.download_request import (
    DownloadRequest,
)


def create_request():

    return DownloadRequest(
        symbol="BTCUSDT",
        interval="1",
        start=datetime(
            2024,
            1,
            1,
            tzinfo=timezone.utc,
        ),
        end=datetime(
            2024,
            1,
            10,
            tzinfo=timezone.utc,
        ),
    )


def test_new_dataset_requires_download():

    state = SynchronizationState(
        exists=False,
        first_timestamp=None,
        last_timestamp=None,
        rows=0,
    )

    plan = SynchronizationPlanner.plan(
        request=create_request(),
        state=state,
    )

    assert plan.download_required is True


def test_existing_complete_dataset_skips_download():

    state = SynchronizationState(
        exists=True,
        first_timestamp=datetime(
            2024,
            1,
            1,
            tzinfo=timezone.utc,
        ),
        last_timestamp=datetime(
            2024,
            1,
            10,
            tzinfo=timezone.utc,
        ),
        rows=100,
    )

    plan = SynchronizationPlanner.plan(
        request=create_request(),
        state=state,
    )

    assert plan.download_required is False