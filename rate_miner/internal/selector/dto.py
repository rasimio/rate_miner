from dataclasses import dataclass
from rate_miner.internal.miner.const import Exchanger


@dataclass
class PairGetBody:
    token_from: str
    token_to: str
    exchanger: Exchanger = None
