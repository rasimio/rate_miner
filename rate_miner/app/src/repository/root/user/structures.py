import datetime
from dataclasses import dataclass
from app.src.database import CRUDTable


@dataclass
class UserTable(CRUDTable):
    id: int
    user_login: str
    user_password: str
    totp: str
    role_id: int
    date_create: datetime.datetime
