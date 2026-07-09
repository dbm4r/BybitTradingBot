class AccountEndpoints:

    def __init__(self, client):

        self.client = client

    def get_wallet_balance(
        self,
        account_type="UNIFIED"
    ):

        timestamp = self.client.timestamp()

        query = f"accountType={account_type}"

        signature = self.client.sign(
            timestamp,
            query
        )

        headers = self.client.headers(
            signature,
            timestamp
        )

        return self.client.request(
            method="GET",
            endpoint="/v5/account/wallet-balance",
            params={
                "accountType": account_type
            },
            headers=headers
        )