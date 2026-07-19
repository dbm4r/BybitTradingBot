class BaseEndpoint:

    def __init__(
        self,
        client,
    ):
        self.client = client

    def get(
        self,
        endpoint: str,
        params: dict | None = None,
        auth: bool = False,
    ):

        return self.client.request(
            method="GET",
            endpoint=endpoint,
            params=params,
            auth=auth,
        )

    def post(
        self,
        endpoint: str,
        body: dict | None = None,
        auth: bool = False,
    ):

        return self.client.request(
            method="POST",
            endpoint=endpoint,
            body=body,
            auth=auth,
        )