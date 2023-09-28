import psycopg2

from rate_miner.pkg.connectors.structures import ConnectionInfo


def create_connection(**kwargs):
    connection_info: ConnectionInfo = kwargs["connection_info"]
    assert type(connection_info) == ConnectionInfo
    conn = psycopg2.connect(
        host=connection_info.host,
        user=connection_info.user,
        password=connection_info.password,
        database=connection_info.database,
        port=connection_info.port,
    )
    return conn
