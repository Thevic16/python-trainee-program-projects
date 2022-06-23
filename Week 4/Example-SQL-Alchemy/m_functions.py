from sqlalchemy import select, Table, String, Column, create_engine, MetaData, \
    Integer
from sqlalchemy.sql import func

engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()
conn = engine.connect()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

employees = Table(
    'employees', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('marks', Integer),
)

print("\n\n Now() \n\n")
result = conn.execute(select([func.now()]))
print(result.fetchone())

print("\n\n Count() \n\n")
result = conn.execute(select([func.count(students.c.id)]))
print(result.fetchone())

# Insert employee table data
"""
conn.execute(employees.insert(), [{"name": "Kamal", "marks": 56},
                                  {"name": "Fernandez", "marks": 85},
                                  {"name": "Sunil", "marks": 62},
                                  {"name": "Kamal", "marks": 76},
                                  ])
"""

print("\n\n max() \n\n")
result = conn.execute(select([func.max(employees.c.marks)]))
print(result.fetchone())

print("\n\n min() \n\n")
result = conn.execute(select([func.min(employees.c.marks)]))
print(result.fetchone())

print("\n\n AVG() \n\n")
result = conn.execute(select([func.avg(employees.c.marks)]))
print(result.fetchone())
