import time
import web3
from abc import ABC
from typing import Optional
from src.internal.miner import UseCase, Exchanger
from src.internal.miner import dto as miner_structures
from uniswap import Uniswap


class UniswapAPI(UseCase, ABC):
    def __init__(self, eth_node: str):
        super(UniswapAPI, self).__init__(name=Exchanger.UNISWAP)
        self.web3 = web3.Web3(web3.HTTPProvider(eth_node))
        self.version = 3
        self.uniswap = Uniswap(version=self.version, web3=self.web3, address=None, private_key=None)

    async def get(self,
                  token_from: str,
                  token_to: str,
                  exchanger: Exchanger = None,
                  time_from: time.time = None,
                  time_to: time.time = None
                  ) -> miner_structures.PairShot:
        eth = "0x0000000000000000000000000000000000000000"
        dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
        print(self.uniswap.get_price_input(eth, dai, 10 ** 18))
        return miner_structures.PairShot(
            TokenFrom=token_from,
            TokenTo=token_to,
            Exchanger="uniswap",
            RelationalRate=0,
            AbsoluteRate=0,
            LiquidityTF=0,
            LiquidityTT=0,
            TimeStamp=0
        )

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
