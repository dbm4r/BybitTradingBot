from datetime import datetime

from runtime.runtime_session import RuntimeSession
from runtime.runtime_state import RuntimeState


class RuntimeLifecycle:

    def __init__(
        self,
        session: RuntimeSession,
    ):

        self.session = session

    def initialize(
        self,
    ) -> None:

        self.session.state = (
            RuntimeState.INITIALIZING
        )

    def synchronize(
        self,
    ) -> None:

        self.session.state = (
            RuntimeState.SYNCHRONIZING
        )

    def start(
        self,
    ) -> None:

        self.session.state = (
            RuntimeState.RUNNING
        )

        self.session.started_at = (
            datetime.now()
        )

    def pause(
        self,
    ) -> None:

        self.session.state = (
            RuntimeState.PAUSED
        )

    def stop(
        self,
    ) -> None:

        self.session.state = (
            RuntimeState.STOPPED
        )

        self.session.stopped_at = (
            datetime.now()
        )

    def error(
        self,
    ) -> None:

        self.session.state = (
            RuntimeState.ERROR
        )