import yaml
from dataclasses import dataclass
from dacite import from_dict
from typing import Dict


@dataclass
class Server:
    AppVersion: str
    Host: str
    Port: int


@dataclass
class PostgreSQL:
    Host: str
    Port: int
    User: str
    Password: str
    DB: str


@dataclass
class BlockChain:
    ETH: str


@dataclass
class Settings:
    Server: Server
    PostgreSQL: PostgreSQL


def load() -> Settings:
    with open("src/config/config.yml", "r") as y:
        data: Dict = yaml.load(y, Loader=yaml.FullLoader)
    return from_dict(data_class=Settings, data=data)
