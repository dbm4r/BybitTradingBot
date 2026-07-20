import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from data.metadata.dataset_metadata import (
    DatasetMetadata,
)
from data.metadata.metadata_service import (
    MetadataService,
)


class JsonMetadataService(
    MetadataService,
):

    def save(
        self,
        metadata: DatasetMetadata,
        filename: str,
    ) -> None:

        path = Path(
            self._metadata_filename(
                filename,
            )
        )

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        data = asdict(
            metadata,
        )

        data["first_timestamp"] = (
            metadata.first_timestamp.isoformat()
        )

        data["last_timestamp"] = (
            metadata.last_timestamp.isoformat()
        )

        data["last_sync"] = (
            metadata.last_sync.isoformat()
        )

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
            )

    def load(
        self,
        filename: str,
    ) -> DatasetMetadata:

        path = Path(
            self._metadata_filename(
                filename,
            )
        )

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(
                file,
            )

        data["first_timestamp"] = (
            datetime.fromisoformat(
                data["first_timestamp"]
            )
        )

        data["last_timestamp"] = (
            datetime.fromisoformat(
                data["last_timestamp"]
            )
        )

        data["last_sync"] = (
            datetime.fromisoformat(
                data["last_sync"]
            )
        )

        return DatasetMetadata(
            **data,
        )

    def exists(
        self,
        filename: str,
    ) -> bool:

        return Path(
            self._metadata_filename(
                filename,
            )
        ).exists()

    @staticmethod
    def _metadata_filename(
        filename: str,
    ) -> str:

        path = Path(
            filename,
        )

        return str(
            path.with_suffix(
                ".meta.json"
            )
        )