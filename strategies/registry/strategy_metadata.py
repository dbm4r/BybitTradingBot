from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class StrategyMetadata:
    """
    Describes a strategy without holding its implementation.
    """

    name: str

    category: str

    version: str = "1.0"

    author: str = "Unknown"

    description: str = ""

    enabled: bool = True

    tags: tuple[str, ...] = field(
        default_factory=tuple,
    )