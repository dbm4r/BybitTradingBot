from enum import Enum


class TimeInForce(Enum):

    GTC = "GTC"   # Good Till Cancelled

    IOC = "IOC"   # Immediate Or Cancel

    FOK = "FOK"   # Fill Or Kill

    DAY = "DAY"