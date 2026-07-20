from data.metadata.dataset_metadata import (
    DatasetMetadata,
)
from data.validation.checksum_validator import (
    ChecksumValidator,
)
from data.validation.validation_result import (
    ValidationResult,
)


class DatasetValidator:

    @staticmethod
    def validate(
        dataframe,
        metadata: DatasetMetadata,
    ) -> ValidationResult:

        if len(dataframe) != metadata.rows:

            return ValidationResult(
                False,
                "Row count mismatch",
            )

        checksum = ChecksumValidator.checksum(
            dataframe,
        )

        if checksum != metadata.checksum:

            return ValidationResult(
                False,
                "Checksum mismatch",
            )

        return ValidationResult(
            True,
        )