from typing import List, Optional

from src.internal.miner.models import Miner
from src.pkg.database import Postgresql


class TransactionCRUD:
    def __init__(self, cursor: Postgresql) -> None:
        self.__cursor = cursor

    async def create(self, tx_id: str, tx_system_type: str) -> None:
        query = """
            insert into transaction(tx_id, tx_system_type)
            values($1, $2);
        """
        await self.__cursor.create(query, tx_id, tx_system_type)

    async def get(self, tx_id: str) -> Optional[Miner]:
        query = """
            select
                transaction.id as "id",
                transaction.tx_id as "tx_id",
                transaction.sender as "sender",
                transaction.receiver as "receiver",
                transaction.amount as "amount",
                transaction.tx_system_type as "tx_system_type",
                transaction.reflector as "reflector",
                transaction.fee as "fee",
                token.name as "token"
            from transaction
            inner join token on transaction.token_id = token.id
            where transaction.tx_id = $1;
        """
        effect = await self.__cursor.fetchrow(query, tx_id)
        if effect is not None:
            return Miner(**effect)
        return effect

    #
    # async def update(self, id: int, reflector: bool) -> None:
    #     query = """
    #         update transaction set reflector = $1
    #         where id = $2;
    #     """
    #     await self.__cursor.fetch(query, reflector, id)
    #
    # async def update_reflector_publisher(self, id: int, reflector: bool) -> None:
    #     query = """
    #         update transaction set reflector_publisher = $1
    #         where id = $2;
    #     """
    #     await self.__cursor.fetch(query, reflector, id)
