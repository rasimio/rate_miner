from typing import List, Dict
from src.internal.miner.usecase import UseCase
from src.internal.miner.usecase import BinanceAPI, OkxAPI, PancakeSwapAPI, UniswapAPI


class MinerUC:
    def __init__(self, miner_ucs: List[UseCase.__subclasses__]):
        self.exchangers: Dict[str, UseCase.__subclasses__] = {}
        for uc in miner_ucs:
            self.exchangers[uc.name] = uc
        print(self.exchangers)
