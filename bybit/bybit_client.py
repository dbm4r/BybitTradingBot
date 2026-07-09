import requests
import hashlib
import hmac
import time
from bybit.endpoints.market import MarketEndpoints
from bybit.endpoints.account import AccountEndpoints
from bybit.endpoints.trade import TradeEndpoints

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
        headers: dict | None = None
    ):

        url = self.base_url + endpoint

        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=body,
            headers=headers
        )

        response.raise_for_status()

        return response.json()
    
    def timestamp(self):

        return str(
            int(time.time() * 1000)
        )
    def sign(
        self,
        timestamp,
        query=""
    ):

        payload = (
            timestamp
            + self.api_key
            + "5000"
            + query
        )

        return hmac.new(
            self.api_secret.encode(),
            payload.encode(),
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

            "Content-Type": "application/json"

        }
    