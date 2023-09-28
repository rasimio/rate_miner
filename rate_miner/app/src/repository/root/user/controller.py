from app.src.database import CRUDModel

from .structures import UserTable
from typing import List


class UserModel(CRUDModel):
    def __init__(self):
        super().__init__(table_name="user", table_type=UserTable)

    def read(self, connection, **kwargs) -> List[UserTable]:
        return super().read(connection=connection, **kwargs)
