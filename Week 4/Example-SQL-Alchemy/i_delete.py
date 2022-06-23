from sqlalchemy.sql.expression import update
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///college.db', echo=True)

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

conn = engine.connect()
stmt = students.delete().where(students.c.lastname == 'Brown')
conn.execute(stmt)
s = students.select()
result = conn.execute(s).fetchall()
for row in result:
    print(row)
