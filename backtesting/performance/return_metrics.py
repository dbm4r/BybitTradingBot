class ReturnMetrics:

    @staticmethod
    def roi(
        initial_balance,
        final_balance
    ):

        return (
            (
                final_balance
                -
                initial_balance
            )
            /
            initial_balance
        ) * 100