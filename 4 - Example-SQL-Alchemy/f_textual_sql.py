# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_textual_sql.htm#

# First form
print("\n First form \n ")
from sqlalchemy import text, bindparam, String, create_engine

engine = create_engine('sqlite:///college.db', echo=True)
conn = engine.connect()

stmt = text("SELECT * FROM students WHERE students.name BETWEEN :x AND :y")

stmt = stmt.bindparams(
    bindparam("x", type_=String),
    bindparam("y", type_=String)
)

result = conn.execute(stmt, {"x": "A", "y": "L"})
for row in result:
    print(row)

# Second form
print("\n Second form \n ")
from sqlalchemy.sql import select

s = select([text("students.name, students.lastname from students")]).where(
    text("students.name between :x and :y"))
result = conn.execute(s, x='A', y='L').fetchall()
for row in result:
    print(row)

# Third form
print("\n Third form \n ")
from sqlalchemy import and_

s = select([text("* from students")]) \
    .where(
    and_(
        text("students.name between :x and :y"),
        text("students.id>6")
    )
)
result = conn.execute(s, x='A', y='L').fetchall()
for row in result:
    print(row)
    