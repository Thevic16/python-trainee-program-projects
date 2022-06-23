# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_connecting_to_database.htm
from sqlalchemy import create_engine

engine = create_engine('sqlite:///college.db', echo=True)
