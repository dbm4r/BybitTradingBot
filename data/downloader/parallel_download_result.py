from dataclasses import dataclass

from data.models.download_result import DownloadResult


@dataclass(slots=True)
class ParallelDownloadResult:

    downloads: list[DownloadResult]

    completed: int

    failed: int