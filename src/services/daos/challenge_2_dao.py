"""
class FriendDAO:
    def __init__(self, connection_str) -> None:
        self._engine: AsyncEngine = create_async

Methods:
1) Fetch


2) Insert
    - Create an Engine with self.engine.begin()

"""
import os
from sqlalchemy import Table, Engine, create_engine, insert
from database.tables import friends_table
import pandas as pd


class FriendDAO:
    def __init__(self, connection_str) -> None:
        self._engine: Engine = create_engine(connection_str)
        self._table: Table = friends_table

    def insert(self, data_1: list[dict[str, str]]) -> None:
        """
        pd.to_records give you back a dict

        """
        with self._engine.begin() as conn:
            conn.execute(insert(self._table), data_1)


if __name__ == "__main__":
    connection_string: str = os.getenv("PANDAS_PRACTICE_URL")
    print(connection_string)
    dao: FriendDAO = FriendDAO(connection_string)
    df: pd.DataFrame = pd.read_csv("csv_files/challenge_1_dataset.csv")
    pd_dict: list[dict[str, str]] = df.to_dict("records")
    dao.insert(pd_dict)
