import psycopg2
import psycopg2.extras
from dataclasses import dataclass, astuple, asdict
from typing import Type, List


@dataclass
class CRUDTable:
    ...


class CRUDModel:
    def __init__(self, table_name: str, table_type: Type[CRUDTable]):
        self.table_name = table_name
        self.keywords = ["offset", "limit", "sort_order", "order_by"]
        self.table_type: Type[CRUDTable.__subclasses__()] = table_type

    def create(self, connection, **kwargs):
        connection = connection
        data: Type[CRUDTable.__subclasses__()] = kwargs[self.table_name]
        cursor = connection.cursor()
        dict_data = asdict(data)
        del dict_data["id"]
        placeholders = ", ".join(["%s"] * len(dict_data))
        columns = ", ".join(dict_data.keys())
        sql = "INSERT INTO \"%s\" ( %s ) VALUES ( %s )" % (
            self.table_name,
            columns,
            placeholders,
        )
        cursor.execute(sql, astuple(data)[1:])
        connection.commit()
        connection.close()

    def read(self, connection, **kwargs) -> List[CRUDTable]:
        query = f'select * from \"{self.table_name}\"'
        query = self.select_filter(query=query, **kwargs)
        print(query)
        connection = connection
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return [self.table_type(**x) for x in rows]

    def update(self, connection, **kwargs):
        query = f"update {self.table_name} SET"
        query = self.update_filter(query=query, **kwargs)
        print(query)
        connection = connection
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, connection, **kwargs):
        query = f"delete from {self.table_name}"
        query = self.select_filter(query=query, **kwargs)
        connection = connection
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    def update_filter(self, query: str, **kwargs) -> str:
        for k, v in kwargs.items():
            if type(v) == str:
                query += f" {k} = \'{v}\',"
            elif type(v) != dict:
                query += f" {k} = {v},"
        query = query[:-1]
        print(query)
        query = self.select_filter(query=query, **(kwargs["where_clause"]))
        return query

    def select_filter(self, query: str, **kwargs) -> str:
        count = 0
        # if "join" in kwargs:

        for k, v in kwargs.items():
            if k in self.keywords:
                continue
            if count == 0:
                if type(v) == str:
                    query += f" WHERE {k} = \'{v}\'"
                elif type(v) == list:
                    query += f" WHERE {k} in ("
                    for w in v:
                        if type(w) == str:
                            query += f"\'{w}\', "
                        else:
                            query += f"{w}, "
                    query = query[:-2]
                    query += ")"
                else:
                    query += f" WHERE {k} = {v}"
            else:
                if type(v) == str:
                    query += f" AND {k} = \'{v}\'"
                elif type(v) == list:
                    query += f" AND {k} in ("
                    for w in v:
                        if type(w) == str:
                            query += f"\'{w}\', "
                        else:
                            query += f"{w}, "
                    query = query[:-2]
                    query += ")"
                else:
                    query += f" AND {k} = {v}"
            count += 1
        if "order_by" in kwargs:
            query += f" ORDER BY {kwargs['order_by']}"
        if "sort_order" in kwargs:
            query += f" {kwargs['sort_order']}"
        if "limit" in kwargs:
            query += f" limit {kwargs['limit']}"
        if "offset" in kwargs:
            query += f" offset {kwargs['offset']}"
        return query
