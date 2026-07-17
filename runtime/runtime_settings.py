from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeSettings:

    heartbeat_interval: int = 30

    scanner_interval: int = 60

    health_check_interval: int = 60

    reconnect_delay: int = 5

    max_reconnect_attempts: int = 10

    shutdown_timeout: int = 15