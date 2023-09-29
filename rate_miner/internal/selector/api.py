from typing import Union

from fastapi import Header
from rate_miner.pkg.clean_fastapi import Routable, get
from rate_miner.pkg.settings import EliseConfigurator


class Selector(Routable):
    def __init__(self, cfg: EliseConfigurator):
        super().__init__(kernel_route="/selector")
        self.cfg = cfg

    @get("/test")
    async def test(self, auth: Union[str, None] = Header(default=None)):
        return {}

