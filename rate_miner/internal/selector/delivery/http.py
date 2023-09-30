from typing import Union
from fastapi import Header
from rate_miner.internal.selector.delivery import HTTPHandler
from rate_miner.internal.selector import dto
from rate_miner.pkg.clean_fastapi import post
from rate_miner.internal.auth import auth_required


class Selector(HTTPHandler):
    def __init__(self):
        super().__init__(kernel_route="/selector")

    @post("/pair/get")
    @auth_required
    async def get(self,
                  data: dto.PairGetBody,
                  auth: Union[str, None] = Header(default=None)):
        return data
