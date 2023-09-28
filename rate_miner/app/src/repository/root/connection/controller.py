from rate_miner.app.src.repository import CRUDModel

from .structures import ConnectionScheme
from typing import List


class ConnectionModel(CRUDModel):
    def __init__(self):
        super().__init__(table_name="connection", table_type=ConnectionScheme)

    def read(self, connection, **kwargs) -> List[ConnectionScheme]:
        return super().read(connection=connection, **kwargs)
