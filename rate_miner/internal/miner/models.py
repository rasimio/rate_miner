import time
from dataclasses import dataclass


@dataclass
class Miner:
    TokenFrom: str
    TokenTo: str
    ExchangerID: int
    Enabled: bool
