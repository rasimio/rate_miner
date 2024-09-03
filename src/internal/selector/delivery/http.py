from typing import Union
from fastapi import Header
from src.internal.selector.delivery import HTTPHandler
from src.internal.selector import dto
from src.pkg.clean_fastapi import post, get
from src.internal.auth import auth_required


class Selector(HTTPHandler):
    def __init__(self):
        super().__init__(kernel_route="/selector")

    @post("/pair/get")
    @auth_required
    async def pair_get(self,
                  data: dto.PairGetBody,
                  auth: Union[str, None] = Header(default=None)):
        return data

    @get("/pair/fetch")
    @auth_required
    async def pair_fetch(self):
        return "hui"