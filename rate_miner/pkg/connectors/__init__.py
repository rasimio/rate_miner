import rate_miner.pkg.connectors.postgresql_connector

from .structures import ConnectionInfo

union_connectors = {"postgresql": postgresql_connector}

__all__ = [
    "ConnectionInfo",
    "union_connectors",
    "postgresql_connector",
]
