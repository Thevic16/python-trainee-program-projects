# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()

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

if __name__ == "__main__":
    meta.create_all(engine)
