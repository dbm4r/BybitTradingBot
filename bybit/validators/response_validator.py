class ResponseValidator:

    @staticmethod
    def validate(
        response: dict,
    ) -> None:

        if not isinstance(
            response,
            dict,
        ):
            raise ValueError(
                "Expected response to be a dictionary."
            )

        required_fields = (
            "retCode",
            "retMsg",
            "result",
        )

        for field in required_fields:

            if field not in response:

                raise ValueError(
                    f"Missing required field '{field}' "
                    "in Bybit response."
                )