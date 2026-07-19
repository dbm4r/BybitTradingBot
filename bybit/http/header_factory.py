class BybitHeaderFactory:

    @staticmethod
    def create(
        api_key: str,
        signature: str,
        timestamp: str,
    ):

        return {
            "X-BAPI-API-KEY": api_key,
            "X-BAPI-TIMESTAMP": timestamp,
            "X-BAPI-RECV-WINDOW": "5000",
            "X-BAPI-SIGN": signature,
            "X-BAPI-SIGN-TYPE": "2",
            "Content-Type": "application/json",
        }