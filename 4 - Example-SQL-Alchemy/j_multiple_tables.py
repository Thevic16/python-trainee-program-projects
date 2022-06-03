# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_multiple_tables.htm

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    ForeignKey
from sqlalchemy.sql import select

engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()
conn = engine.connect()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

addresses = Table(
    'addresses', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('postal_add', String),
    Column('email_add', String))

# meta.create_all(engine)
'''
conn.execute(students.insert(), [
    {'name': 'Ravi', 'lastname': 'Kapoor'},
    {'name': 'Rajiv', 'lastname': 'Khanna'},
    {'name': 'Komal', 'lastname': 'Bhandari'},
    {'name': 'Abdul', 'lastname': 'Sattar'},
    {'name': 'Priya', 'lastname': 'Rajhans'},
])

conn.execute(addresses.insert(), [
    {'st_id': 1, 'postal_add': 'Shivajinagar Pune',
     'email_add': 'ravi@gmail.com'},
    {'st_id': 1, 'postal_add': 'ChurchGate Mumbai',
     'email_add': 'kapoor@gmail.com'},
    {'st_id': 3, 'postal_add': 'Jubilee Hills Hyderabad',
     'email_add': 'komal@gmail.com'},
    {'st_id': 5, 'postal_add': 'MG Road Bangaluru',
     'email_add': 'as@yahoo.com'},
    {'st_id': 2, 'postal_add': 'Cannought Place new Delhi',
     'email_add': 'admin@khanna.com'},
])
'''

s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
result = conn.execute(s)

for row in result:
    print(row)
