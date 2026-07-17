from enum import Enum


class RuntimeState(Enum):

    STOPPED = "STOPPED"

    INITIALIZING = "INITIALIZING"

    SYNCHRONIZING = "SYNCHRONIZING"

    RUNNING = "RUNNING"

    PAUSED = "PAUSED"

    STOPPING = "STOPPING"

    ERROR = "ERROR"