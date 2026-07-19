import json

from config import HTTP_DEBUG


class RequestLogger:

    @staticmethod
    def log(
        method,
        url,
        headers,
        params,
        body,
    ):

        if not HTTP_DEBUG:
            return

        print("\n========== BYBIT REQUEST ==========")
        print(f"METHOD : {method}")
        print(f"URL    : {url}")

        if params:
            print("PARAMS:")
            print(
                json.dumps(
                    params,
                    indent=4,
                )
            )

        if body:
            print("BODY:")
            print(
                json.dumps(
                    body,
                    indent=4,
                )
            )

        print("HEADERS:")
        print(
            json.dumps(
                headers or {},
                indent=4,
            )
        )

        print("===================================\n")