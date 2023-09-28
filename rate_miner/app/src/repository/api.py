import hashlib
from typing import List

from fastapi import HTTPException

from rate_miner.app.src.repository.root import FullScheme
from rate_miner.app.src.repository.root.connection import ConnectionModel, ConnectionScheme
from rate_miner.pkg.clean_fastapi import Routable, post
from rate_miner.pkg.connectors import ConnectionInfo, union_connectors
from rate_miner.pkg.encryption_shield import InvalidToken, Shield

from .structures import EncryptionKeyBody


class Arrow(Routable):
    def __init__(self, hash_key: str, decrypt_phrase: str, elisabeth: FullScheme):
        super().__init__(kernel_route="/arrow")
        self._key = ""
        self._hash_key = hash_key
        self._decrypt_phrase = decrypt_phrase
        self.connections: List[ConnectionScheme] = []
        self.elisabeth = elisabeth
        self.connection_model = ConnectionModel()
        self.load_connections()

    def get_key(self):
        return self._key

    @post("/load_encryption_key")
    async def load_encryption_key(self, data: EncryptionKeyBody):
        if (
                hashlib.sha512(str(data.time_stamp).encode("UTF-8") + self._hash_key.encode("UTF-8")).hexdigest()
                == data.signature
        ):
            try:
                Shield.decrypt_by_key(message=self._decrypt_phrase, key=data.key)
            except InvalidToken:
                raise HTTPException(status_code=422)
            self._key = data.key
        else:
            raise HTTPException(status_code=401)

    def encrypt(self, message: str) -> str:
        return Shield.encrypt_by_key(message=message, key=self._key)

    def decrypt(self, message: str) -> str:
        return Shield.decrypt_by_key(message=message, key=self._key)

    def load_connections(self):
        conn = self.connect_to_scheme()
        self.connections = self.connection_model.read(
            connection=conn,
        )

    def connect_to_scheme(self):
        return union_connectors[self.elisabeth.db_type].create_connection(
            connection_info=self.elisabeth.connection_info,
        )

    def create_connection(self, connection_id: int):
        for connection in self.connections:
            if connection.id == connection_id:
                return union_connectors[connection.type_label].create_connection(
                    connection_info=ConnectionInfo(
                        host=connection.db_host,
                        password=connection.db_password,
                        user=connection.db_user,
                        auth_plugin=connection.db_auth_plugin,
                        database=connection.db_name,
                        port=connection.db_port,
                    ),
                )
