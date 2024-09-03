import time
from abc import ABC
from typing import Optional
from src.internal.miner import UseCase, Exchanger
from src.internal.miner import dto as miner_structures


class PancakeSwapAPI(UseCase, ABC):
    def __init__(self):
        super(PancakeSwapAPI, self).__init__(Exchanger.PANCAKESWAP)

    async def get(self,
                  token_from: str,
                  token_to: str,
                  exchanger: Exchanger = None,
                  time_from: time.time = None,
                  time_to: time.time = None
                  ) -> miner_structures.PairShot:
        pass

    async def fetch(self,
                    token_from: str,
                    token_to: str,
                    time_from: time.time = None,
                    time_to: time.time = None,
                    limit: int = None
                    ) -> miner_structures.PairTimeLine:
        pass

    async def save(self,
                   pair: Optional[miner_structures.PairShot, miner_structures.PairTimeLine] = None) -> None:
        pass
