"""This is sample usage SqlAlchemy."""
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    Numeric,
    String,
    ForeignKey,
)

# from sqlalchemy.dialects.postgresql import JSON

# sqlite
engine = create_engine("sqlite:///:memory:",echo=True)
#dialect+driver://user:password@host:port/db
# engine = create_engine('sqlite:///cookies.db')
# engine = create_engine('sqlite:///:memory:')
# engine = create_engine("postgresql+psycopg2://username:password@localhost:5432/my_db")
# engine = create_engine("mysql+pymysql://username:password@localhost/my_db", pool_recycle=3600)
engine.
connetct
execute
begin
dispose
driver
table_names
transaction
"""
SQLAlchemy  Python              SQL
----------  ------              ---
BigInteger  int                 BIGINT
Boolean     bool                BOOLEAN or SMALLINT
Date        datetime.date       DATE (SQLite: STRING )
DateTime    datetime.datetime   DATETIME (SQLite: STRING )
Enum        str                 ENUM or VARCHAR
Float       float or Decimal    FLOAT or REAL
Integer     int                 INTEGER
Interval    datetime.timedelta  INTERVAL or DATE from epoch
LargeBinary byte                BLOB or BYTEA
Numeric     decimal.Decimal     NUMERIC or DECIMAL
Unicode     unicode             UNICODE or VARCHAR
Text        str                 CLOB or TEXT
Time        datetime.time       DATETIME
"""


metadata = MetaData()


cookies = Table(
    "cookies",
    metadata,
    Column("cookie_id", Integer(), primary_key=True),
    Column("name", String(50), index=True),
    Column("recipe_URL", String(255)),
    Column("sku", String(55)),
    Column("quantity", Integer()),
    Column("unit_cost", Numeric(12, 2)),
)

cookies.create_all(engine)

#---------------------------------------
cookies.insert()
ins=insert().values(name='Karen',last='Gram')
str(ins)
ins.compile().params
update()
delete()
select()

conn = engine.connect()
res = conn.execute(ins)
res.inserted_primary_key
conn.execute(stu.insert(),[{'a':'a_1'},
                           {'a':'a_2'}])

#--------------
stu.select()
conn = engine.connect()
res = conn.execute(s)
for r in res:
    pass# (id,name,...)

s=stu.select().where(stu.c.id > 2)#c is a alias for column
conn.execute(s)
#------------------
from sqlalchemy.sql import select
s = select([users])
res = conn.execute(s)
#--------------------

