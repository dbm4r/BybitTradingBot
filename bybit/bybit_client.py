import requests
import hashlib
import hmac
import time
from bybit.endpoints.market import MarketEndpoints
from bybit.endpoints.account import AccountEndpoints
from bybit.endpoints.trade import TradeEndpoints
import json

class BybitClient:

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        base_url: str
    ):

        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.market = MarketEndpoints(self)
        self.account = AccountEndpoints(self)
        self.trade = TradeEndpoints(self)

    def request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        body: dict | None = None,
        auth: bool = False
    ):

        url = self.base_url + endpoint

        headers = None

        if auth:

            timestamp = self.timestamp()

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

                json_body = json.dumps(
                    body or {},
                    separators=(",", ":")
                )

                payload = (
                    timestamp
                    + self.api_key
                    + "5000"
                    + json_body
                )

            signature = self.sign(payload)

            headers = self.headers(
                signature,
                timestamp
            )

        request_kwargs = {
            "method": method,
            "url": url,
            "headers": headers
        }

        if params is not None:
            request_kwargs["params"] = params

        if body is not None:

            json_body = json.dumps(
                body,
                separators=(",", ":")
            )

            request_kwargs["data"] = json_body

        response = requests.request(
            **request_kwargs
        )

        response.raise_for_status()

        return response.json()
    
    def timestamp(self):

        return str(
            int(time.time() * 1000)
        )
    def sign(
        self,
        payload: str
    ):

        return hmac.new(
            self.api_secret.encode("utf-8"),
            payload.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
    def headers(
        self,
        signature,
        timestamp
    ):

        return {

            "X-BAPI-API-KEY": self.api_key,

            "X-BAPI-TIMESTAMP": timestamp,

            "X-BAPI-RECV-WINDOW": "5000",

            "X-BAPI-SIGN": signature,

            "X-BAPI-SIGN-TYPE": "2",

            "Content-Type": "application/json"

        }
    