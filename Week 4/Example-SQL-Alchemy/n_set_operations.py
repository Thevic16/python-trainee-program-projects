from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
   union, union_all, except_, intersect

engine = create_engine('sqlite:///college.db', echo=True)

meta = MetaData()
conn = engine.connect()
addresses = Table(
    'addresses', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer),
    Column('postal_add', String),
    Column('email_add', String)
)

print(" \n\n Union \n\n")
u = union(addresses.select().where(addresses.c.email_add.like('%@gmail.com')),
          addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))

result = conn.execute(u)
print(result.fetchall())

print(" \n\n UNION ALL \n\n")
u = union_all(
    addresses.select().where(addresses.c.email_add.like('%@gmail.com')),
    addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))

result = conn.execute(u)
print(result.fetchall())

print(" \n\n EXCEPT \n\n")
u = except_(addresses.select().where(addresses.c.email_add.like('%@gmail.com'))
            , addresses.select().where(addresses.c.postal_add.like('%Pune')))

result = conn.execute(u)
print(result.fetchall())

print(" \n\n INTERSECT \n\n")
u = intersect(
    addresses.select().where(addresses.c.email_add.like('%@gmail.com'))
    , addresses.select().where(addresses.c.postal_add.like('%Pune')))

result = conn.execute(u)
print(result.fetchall())
