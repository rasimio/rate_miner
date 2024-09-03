import yaml
from dataclasses import dataclass
from typing import Dict


@dataclass
class Server:
    AppVersion: str
    Host: str
    Port: str


@dataclass
class PostgreSQL:
    Host: str
    Port: str
    User: str
    Password: str
    DB: str


@dataclass
class Settings:
    Server: Server
    PostgreSQL: PostgreSQL
