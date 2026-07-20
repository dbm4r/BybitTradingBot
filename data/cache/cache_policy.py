from enum import Enum


class CachePolicy(Enum):

    LRU = "lru"

    FIFO = "fifo"