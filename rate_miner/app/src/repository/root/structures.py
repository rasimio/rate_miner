from dataclasses import dataclass

from rate_miner.pkg.connectors import ConnectionInfo


@dataclass
class Scheme:
    connection: str
    wallet: str
    transaction: str
    user: str
    totp_token: str
    person_white_list: str


@dataclass
class FullScheme:
    table_info: Scheme
    db_type: str
    connection_info: ConnectionInfo
