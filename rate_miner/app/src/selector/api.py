import datetime
import time
import traceback
from typing import Dict, List, Union

from fastapi import Header, HTTPException
from rate_miner.app.src.repository.api import Arrow
from rate_miner.app.src.auth.api import Auth
from rate_miner.pkg.clean_fastapi import Routable, get, post
from rate_miner.pkg.settings import EliseConfigurator


class Selector(Routable):
    def __init__(self, cfg: EliseConfigurator, auth: Auth, arrow: Arrow):
        super().__init__(kernel_route="/selector")
        self.cfg = cfg
        self.auth = auth
        self.arrow = arrow

    @get("/test")
    async def test(self, auth: Union[str, None] = Header(default=None)):
        await self.auth.authenticate(auth_header=auth)
        return {}

