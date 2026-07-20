from data.storage.csv_storage import CsvStorage
from data.storage.parquet_storage import (
    ParquetStorage,
)
from data.storage.storage import Storage
from data.storage.storage_type import (
    StorageType,
)


class StorageFactory:

    @staticmethod
    def create(
        storage_type: (
            StorageType | str
        ) = StorageType.CSV,
    ) -> Storage:

        if isinstance(
            storage_type,
            str,
        ):

            storage_type = StorageType(
                storage_type.lower()
            )

        match storage_type:

            case StorageType.CSV:

                return CsvStorage()

            case StorageType.PARQUET:

                return ParquetStorage()

        raise ValueError(
            f"Unsupported storage type: "
            f"{storage_type}"
        )