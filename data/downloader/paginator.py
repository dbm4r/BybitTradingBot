from datetime import timedelta

from data.downloader.download_job import DownloadJob
from data.downloader.interval import Interval
from data.downloader.page import Page


class Paginator:

    def __init__(
        self,
        job: DownloadJob,
    ):

        self.job = job

        self.current = job.start

        self.interval = Interval.from_code(
            job.interval
        )

    def __iter__(
        self,
    ):

        return self

    def __next__(
        self,
    ) -> Page:

        if self.current >= self.job.end:
            raise StopIteration

        candle_span = (
            self.interval.milliseconds
            * self.job.page_size
        )

        page_end = self.current + timedelta(
            milliseconds=candle_span
        )

        if page_end > self.job.end:
            page_end = self.job.end

        page = Page(
            start=self.current,
            end=page_end,
            limit=self.job.page_size,
        )

        self.current = page_end

        return page