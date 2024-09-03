import time
from ..const import Exchanger
from ..dto import PairShot, PairTimeLine
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from src.internal.miner.usecase.binance import BinanceAPI
from src.internal.miner.usecase.okx import OkxAPI
from src.internal.miner.usecase.pancakeswap import PancakeSwapAPI
from src.internal.miner.usecase.uniswap import UniswapAPI

__all__ = ["BinanceAPI", "OkxAPI", "PancakeSwapAPI", "UniswapAPI"]


class UseCase(ABC):
    def __init__(self, name: Exchanger):
        self.name = name

    @abstractmethod
    async def get(self,
                  token_from: str,
                  token_to: str,
                  exchanger: Exchanger = None,
                  time_from: time.time = None,
                  time_to: time.time = None
                  ) -> PairShot:
        pass

    @abstractmethod
    async def fetch(self,
                    token_from: str,
                    token_to: str,
                    time_from: time.time = None,
                    time_to: time.time = None,
                    limit: int = None
                    ) -> PairTimeLine:
        pass

    @abstractmethod
    async def save(self,
                   pair: Optional[PairShot] = None) -> None:
        pass
