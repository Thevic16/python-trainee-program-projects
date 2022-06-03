# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_executing_expression.htm
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

# Insert One row.
'''
ins = students.insert().values(name='Jaylen', lastname='Brown')
result = conn.execute(ins)
print(result.inserted_primary_key)
'''

# Insert Multiples rows.
conn.execute(students.insert(), [
    {'name': 'Rajiv', 'lastname': 'Khanna'},
    {'name': 'Komal', 'lastname': 'Bhandari'},
    {'name': 'Abdul', 'lastname': 'Sattar'},
    {'name': 'Priya', 'lastname': 'Rajhans'},
])
