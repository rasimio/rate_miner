import datetime
from dataclasses import dataclass
from app.src.database import CRUDTable


@dataclass
class WalletTable(CRUDTable):
    id: int
    account: str
    access_token: str
    p2p_token: str
    owner_first_name: str
    owner_last_name: str
    owner_middle_name: str
    balance: float
    date_create: datetime.datetime
    status: str
    user_id: int
