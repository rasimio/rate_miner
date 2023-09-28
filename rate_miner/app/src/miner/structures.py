import time
from dataclasses import dataclass
from typing import List


@dataclass
class PairShot:
    TokenFrom: str
    TokenTo: str
    Exchanger: str
    RelationalRate: float
    AbsoluteRate: float
    LiquidityTF: float  # liquidity in value of token from
    LiquidityTT: float  # liquidity in value of token to
    TimeStamp: time.time


@dataclass
class PairTimeLine:
    Start: time.time
    End: time.time
    TokenFrom: str
    TokenTo: str
    Sequence: List[PairShot]
