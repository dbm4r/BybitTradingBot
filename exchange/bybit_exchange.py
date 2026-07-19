from exchange.exchange import Exchange
from exchange.exchange_operation import ExchangeOperation
from exchange.exchange_result import ExchangeResult
from exchange.exchange_snapshot import ExchangeSnapshot
from exchange.exchange_symbol import ExchangeSymbol
from exchange.instrument_service import InstrumentService

from market.market_data_provider import MarketDataProvider

from bybit.bybit_client import BybitClient

from bybit.parsers.balance_parser import BybitBalanceParser
from bybit.parsers.order_parser import BybitOrderParser
from bybit.parsers.position_parser import BybitPositionParser
from bybit.parsers.symbol_parser import BybitSymbolParser
from bybit.parsers.trade_parser import BybitTradeParser


class BybitExchange(
    Exchange,
    MarketDataProvider,
):

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        **_,
    ):

        self.client = BybitClient(
            api_key=api_key,
            api_secret=api_secret,
        )

        self.instrument_service = InstrumentService(
            self.client,
        )

    def get_instrument(
        self,
        symbol: str,
    ):

        return self.instrument_service.get(
            symbol,
        )

    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price=None,
    ):

        response = self.client.trade.place_market_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
        )

        exchange_order = BybitOrderParser.parse_create_order(
            response=response,
            symbol=symbol,
            side=side,
            quantity=quantity,
        )

        return ExchangeResult(
            success=True,
            order=exchange_order,
        )

    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float,
    ):

        response = self.client.trade.place_limit_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price,
        )

        exchange_order = BybitOrderParser.parse_create_order(
            response=response,
            symbol=symbol,
            side=side,
            quantity=quantity,
        )

        return ExchangeResult(
            success=True,
            order=exchange_order,
        )

    def cancel_order(
        self,
        symbol: str,
        order_id: str,
    ):

        response = self.client.trade.cancel_order(
            symbol=symbol,
            order_id=order_id,
        )

        return ExchangeOperation(
            success=True,
            message=response["retMsg"],
            raw_response=response,
        )

    def amend_order(
        self,
        symbol: str,
        order_id: str,
        price: float | None = None,
        quantity: float | None = None,
    ):

        response = self.client.trade.amend_order(
            symbol=symbol,
            order_id=order_id,
            price=price,
            quantity=quantity,
        )

        return ExchangeOperation(
            success=True,
            message=response["retMsg"],
            raw_response=response,
        )

    def set_trading_stop(
        self,
        symbol: str,
        take_profit: float,
        stop_loss: float,
    ):

        response = self.client.trade.set_trading_stop(
            symbol=symbol,
            take_profit=take_profit,
            stop_loss=stop_loss,
        )

        return ExchangeOperation(
            success=True,
            message=response["retMsg"],
            raw_response=response,
        )

    def get_balance(
        self,
    ):

        response = self.client.account.get_wallet_balance()

        return BybitBalanceParser.parse(
            response,
        )

    def get_positions(
        self,
    ):

        response = self.client.trade.get_positions()

        return BybitPositionParser.parse_list(
            response,
        )

    def get_open_orders(
        self,
        symbol: str | None = None,
    ):

        response = self.client.trade.get_open_orders(
            symbol=symbol,
        )

        return BybitOrderParser.parse_open_orders(
            response,
        )

    def get_order(
        self,
        order_id: str,
    ):

        response = self.client.trade.get_order(
            order_id=order_id,
        )

        return BybitOrderParser.parse_order(
            response,
        )

    def get_trade_history(
        self,
    ):

        response = self.client.trade.get_trade_history()

        return BybitTradeParser.parse_list(
            response,
        )

    def create_snapshot(
        self,
    ):

        return ExchangeSnapshot(
            balance=self.get_balance(),
            positions=self.get_positions(),
            orders=self.get_open_orders(),
            trades=self.get_trade_history(),
        )

    def get_symbols(
        self,
    ) -> list[ExchangeSymbol]:

        response = self.client.market.get_instruments()

        return BybitSymbolParser.parse_list(
            response,
        )

    def get_candles(
        self,
        symbol: str,
        interval: str,
        limit: int = 200,
    ):

        return self.client.market.get_kline(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )