from dataclasses import dataclass
from rate_miner.app.src.repository import CRUDTable


@dataclass
class ConnectionScheme(CRUDTable):
    id: int
    db_host: str
    db_user: str
    db_password: str
    db_name: str
    db_auth_plugin: str
    db_port: str
    type_label: str
