from app.src.database import CRUDModel
from .structures import SessionTable
from typing import List


class SessionModel(CRUDModel):
    def __init__(self):
        super().__init__(table_name="session", table_type=SessionTable)

    def read(self, connection, **kwargs) -> List[SessionTable]:
        return super().read(connection=connection, **kwargs)