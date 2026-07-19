import json

from config import HTTP_DEBUG


class ResponseLogger:

    MAX_LIST_ITEMS = 5

    @staticmethod
    def log(
        response,
    ):

        if not HTTP_DEBUG:
            return

        print("\n========== BYBIT RESPONSE ==========")

        result = response.get("result")

        if (
            isinstance(result, dict)
            and isinstance(result.get("list"), list)
            and len(result["list"]) > ResponseLogger.MAX_LIST_ITEMS
        ):

            preview = dict(response)
            preview["result"] = dict(result)
            preview["result"]["list"] = result["list"][
                : ResponseLogger.MAX_LIST_ITEMS
            ]
            preview["result"]["truncated"] = True
            preview["result"]["total_items"] = len(
                result["list"]
            )

            print(
                json.dumps(
                    preview,
                    indent=4,
                )
            )

        else:

            print(
                json.dumps(
                    response,
                    indent=4,
                )
            )

        print("====================================\n")