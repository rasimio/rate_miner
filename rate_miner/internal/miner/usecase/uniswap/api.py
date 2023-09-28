import time
from abc import ABC
from typing import Optional
from rate_miner.internal.miner import UseCase, Exchanger
from rate_miner.internal.miner import models as miner_structures


class UniswapAPI(UseCase, ABC):
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
