class MarketExecutor:

    @staticmethod
    def prepare_buy(engine):

        fee = (
            engine.portfolio.cash
            * engine.settings.trading_fee
        )

        cash_after_fee = (
            engine.portfolio.cash - fee
        )

        engine.total_fees += fee

        return cash_after_fee