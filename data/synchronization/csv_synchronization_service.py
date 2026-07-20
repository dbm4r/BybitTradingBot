from data.metadata.metadata_service import (
    MetadataService,
)
from data.synchronization.synchronization_service import (
    SynchronizationService,
)
from data.synchronization.synchronization_state import (
    SynchronizationState,
)


class CsvSynchronizationService(
    SynchronizationService,
):

    def __init__(
        self,
        metadata_service: MetadataService,
    ):

        self.metadata_service = metadata_service

    def inspect(
        self,
        filename: str,
    ) -> SynchronizationState:

        if not self.metadata_service.exists(
            filename,
        ):

            return SynchronizationState(
                exists=False,
                first_timestamp=None,
                last_timestamp=None,
                rows=0,
            )

        metadata = self.metadata_service.load(
            filename,
        )

        return SynchronizationState(
            exists=True,
            first_timestamp=metadata.first_timestamp,
            last_timestamp=metadata.last_timestamp,
            rows=metadata.rows,
        )