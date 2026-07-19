import json

from bybit.http.header_factory import BybitHeaderFactory
from bybit.http.timestamp import Timestamp


class BybitAuthenticator:

    def __init__(
        self,
        api_key: str,
        signer,
    ):
        self.api_key = api_key
        self.signer = signer

    def create_headers(
        self,
        method: str,
        params: dict | None = None,
        body: dict | None = None,
    ):

        timestamp = Timestamp.now()

        if method.upper() == "GET":

            query = ""

            if params:

                query = "&".join(
                    f"{key}={value}"
                    for key, value in params.items()
                )

            payload = (
                timestamp
                + self.api_key
                + "5000"
                + query
            )

        else:

            payload = (
                timestamp
                + self.api_key
                + "5000"
                + json.dumps(
                    body or {},
                    separators=(",", ":"),
                )
            )

        signature = self.signer.sign(
            payload
        )

        return BybitHeaderFactory.create(
            api_key=self.api_key,
            signature=signature,
            timestamp=timestamp,
        )