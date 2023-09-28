from dataclasses import dataclass


@dataclass
class ConnectionInfo:
    host: str
    user: str
    password: str
    database: str
    auth_plugin: str
    port: str
