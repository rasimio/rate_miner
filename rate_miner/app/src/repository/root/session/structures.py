import datetime
from dataclasses import dataclass
from rate_miner.app.src.repository import CRUDTable


@dataclass
class SessionTable(CRUDTable):
    id: int
    session_key: str
    user_id: int
    date_create: datetime.datetime
