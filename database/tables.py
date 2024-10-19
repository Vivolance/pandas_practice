from sqlalchemy import Table, MetaData, Column, TEXT, INT

"""
CREATE TABLE friends(
    NAME TEXT PRIMARY KEY,
    AGE INT NOT NULL,
    TOWN TEXT NOT NULL
)
"""

metadata: MetaData = MetaData()


friends_table: Table = Table(
    "friends",
    metadata,
    Column("NAME", TEXT, primary_key=True),
    Column("AGE", INT, nullable=False),
    Column("TOWN", TEXT, nullable=False)
)