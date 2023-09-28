import datetime
from dataclasses import dataclass
from typing import Optional
from app.src.database import CRUDTable


@dataclass
class TransactionTable(CRUDTable):
    id: int
    qiwi_id: str
    date_create: datetime.datetime
    receiver: str
    success: bool
    user_id: int
    receive_code: Optional[str]
    amount: float
    amount_rub: float
    currency_id: int
    wallet_id: int
