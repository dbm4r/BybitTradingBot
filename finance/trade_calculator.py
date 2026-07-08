class TradeCalculator:

    @staticmethod
    def exit_value(
        quantity: float,
        exit_price: float
    ) -> float:

        return quantity * exit_price

    @staticmethod
    def entry_value(
        quantity: float,
        entry_price: float
    ) -> float:

        return quantity * entry_price

    @staticmethod
    def fee(
        value: float,
        fee_rate: float
    ) -> float:

        return value * fee_rate

    @staticmethod
    def cash_received(
        exit_value: float,
        fee: float
    ) -> float:

        return exit_value - fee

    @staticmethod
    def gross_profit(
        entry_value: float,
        exit_value: float
    ) -> float:

        return exit_value - entry_value

    @staticmethod
    def net_profit(
        gross_profit: float,
        fee: float
    ) -> float:

        return gross_profit - fee

    @staticmethod
    def profit_percent(
        net_profit: float,
        entry_value: float
    ) -> float:

        return (net_profit / entry_value) * 100
    @staticmethod
    def position_cost(
        quantity: float,
        price: float
    ) -> float:

        return quantity * price
    @staticmethod
    def unrealized_profit(
        quantity: float,
        entry_price: float,
        current_price: float
    ) -> float:

        return quantity * (
            current_price - entry_price
        )
    @staticmethod
    def roi(
        initial_balance: float,
        final_balance: float
    ) -> float:

        return (
            (final_balance - initial_balance)
            / initial_balance
        ) * 100
    @staticmethod
    def risk_reward_ratio(
        entry_price: float,
        stop_price: float,
        target_price: float
    ) -> float:

        risk = entry_price - stop_price
        reward = target_price - entry_price

        if risk == 0:
            return 0

        return reward / risk
    @staticmethod
    def long_profit(
        entry_price: float,
        exit_price: float,
        quantity: float
    ) -> float:

        return (
            exit_price - entry_price
        ) * quantity