import json
from bybit.validators.response_validator import (
    ResponseValidator,
)
from config import BYBIT_TESTNET
from bybit.exception_mapper import BybitExceptionMapper
from bybit.endpoints.account import AccountEndpoints
from bybit.endpoints.market import MarketEndpoints
from bybit.endpoints.trade import TradeEndpoints
from bybit.http.authenticator import BybitAuthenticator
from bybit.http.http_client import HttpClient
from bybit.http.request_logger import RequestLogger
from bybit.http.response_logger import ResponseLogger
from bybit.http.signer import BybitSigner


class BybitClient:

    def __init__(
        self,
        api_key: str,
        api_secret: str,
    ):

        self.api_key = api_key
        self.api_secret = api_secret

        if BYBIT_TESTNET:
            self.base_url = "https://api-testnet.bybit.com"
        else:
            self.base_url = "https://api.bybit.com"

        self.http = HttpClient()

        self.signer = BybitSigner(
            api_secret=api_secret,
        )

        self.authenticator = BybitAuthenticator(
            api_key=api_key,
            signer=self.signer,
        )

        self.market = MarketEndpoints(self)
        self.account = AccountEndpoints(self)
        self.trade = TradeEndpoints(self)

    def request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        body: dict | None = None,
        auth: bool = False,
    ):

        url = self.base_url + endpoint

        headers = None

        if auth:

            headers = self.authenticator.create_headers(
                method=method,
                params=params,
                body=body,
            )

        RequestLogger.log(
            method=method,
            url=url,
            headers=headers,
            params=params,
            body=body,
        )

        response = self.http.send(
            method=method,
            url=url,
            headers=headers,
            params=params,
            body=body,
        )

        ResponseLogger.log(
            response,
        )
        ResponseValidator.validate(
            response,
        )
        BybitExceptionMapper.raise_for_response(
            response,
        )

        return response