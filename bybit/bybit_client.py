import requests


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
    def get_server_time(self):

        return self.request(
            method="GET",
            endpoint="/v5/market/time"
        )