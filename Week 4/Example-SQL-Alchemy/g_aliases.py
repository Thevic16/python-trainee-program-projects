from sqlalchemy import create_engine
from sqlalchemy.sql import alias, select
from c_creating_table import students

engine = create_engine('sqlite:///college.db', echo=True)
conn = engine.connect()

st = students.alias("a")
s = select([st]).where(st.c.id > 2)
result = conn.execute(s).fetchall()

for row in result:
    print(row)
