from abc import ABC, abstractmethod
from fastapi import Header
from typing import Union
from src.pkg.clean_fastapi import Routable
from src.internal.selector import dto


class HTTPHandler(Routable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    async def get(self,
                  data: dto.PairGetBody,
                  auth: Union[str, None] = Header(default=None)):
        """

        :param data:
        :param auth:
        :return:
        """
        pass
