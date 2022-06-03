# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_conjunctions.htm

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    ForeignKey, select

engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()
conn = engine.connect()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)


from sqlalchemy import and_, or_, asc, desc, between

'''
stmt = select([students]).where(and_(students.c.name == 'Ravi',
 students.c.id < 3))

stmt = select([students]).where(or_(students.c.name == 'Ravi',
 students.c.id <3))
 
stmt = select([students]).order_by(asc(students.c.name))
stmt = select([students]).order_by(desc(students.c.lastname))

'''
stmt = select([students]).where(between(students.c.id, 2, 4))

result = conn.execute(stmt)
print(result.fetchall())
