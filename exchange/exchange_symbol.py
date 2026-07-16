from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ExchangeSymbol:

    symbol: str

    base_coin: str

    quote_coin: str

    status: str

    tick_size: float

    qty_step: float

    min_order_qty: float

    max_order_qty: float

    is_tradable: bool