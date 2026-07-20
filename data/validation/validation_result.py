from dataclasses import dataclass


@dataclass(slots=True)
class ValidationResult:

    valid: bool

    message: str | None = None