from app.src.database import CRUDModel

from .structures import WalletTable
from typing import List


class WalletModel(CRUDModel):
    def __init__(self):
        super().__init__(table_name="wallet", table_type=WalletTable)

    def read(self, connection, **kwargs) -> List[WalletTable]:
        return super().read(connection=connection, **kwargs)
