from app.src.database import CRUDModel
import psycopg2
import psycopg2.extras
from dataclasses import dataclass, astuple, asdict
from typing import Type, List
from .structures import TransactionTable
from typing import List


class TransactionModel(CRUDModel):
    def __init__(self):
        super().__init__(table_name="transaction", table_type=TransactionTable)

    def read(self, connection, **kwargs) -> List[TransactionTable]:
        query = f'select * from \"{self.table_name}\" inner join wallet'
        query = self.select_filter(query=query, **kwargs)
        print(query)
        connection = connection
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return [TransactionTable(**x) for x in rows]
