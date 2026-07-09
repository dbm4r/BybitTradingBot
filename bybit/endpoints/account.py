class AccountEndpoints:

    def __init__(self, client):

        self.client = client

    def get_wallet_balance(
        self,
        account_type="UNIFIED"
    ):

        return self.client.request(
            method="GET",
            endpoint="/v5/account/wallet-balance",
            params={
                "accountType": account_type
            },
            auth=True
        )