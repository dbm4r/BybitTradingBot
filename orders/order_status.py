from enum import Enum


class OrderStatus(Enum):

    PENDING = "Pending"

    FILLED = "Filled"

    CANCELLED = "Cancelled"

    REJECTED = "Rejected"