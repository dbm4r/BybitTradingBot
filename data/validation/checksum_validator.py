from hashlib import sha256

import pandas as pd


class ChecksumValidator:

    @staticmethod
    def checksum(
        dataframe: pd.DataFrame,
    ) -> str:

        return sha256(
            dataframe.to_csv(
                index=False,
            ).encode()
        ).hexdigest()