import hashlib
import hmac
import time


class WebSocketAuth:

    def __init__(
        self,
        api_key,
        api_secret
    ):
        self.api_key = api_key
        self.api_secret = api_secret

    def generate(self):

        expires = str(
            int((time.time() + 10) * 1000)
        )

        signature = hmac.new(
            self.api_secret.encode(),
            f"GET/realtime{expires}".encode(),
            hashlib.sha256
        ).hexdigest()

        return {
            "op": "auth",
            "args": [
                self.api_key,
                expires,
                signature
            ]
        }