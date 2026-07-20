from dataclasses import dataclass

from data.models.download_request import DownloadRequest


@dataclass(slots=True)
class ParallelDownloadRequest:

    requests: list[DownloadRequest]

    max_workers: int = 4