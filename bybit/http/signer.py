import hashlib
import hmac


class BybitSigner:

    def __init__(
        self,
        api_secret: str,
    ):
        self.api_secret = api_secret

    def sign(
        self,
        payload: str,
    ) -> str:

        return hmac.new(
            self.api_secret.encode("utf-8"),
            payload.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()