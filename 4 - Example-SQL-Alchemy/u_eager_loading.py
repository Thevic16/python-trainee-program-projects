# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_eager_loading.htm
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String

engine = create_engine('sqlite:///sales.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="invoices")


Customer.invoices = relationship("Invoice", order_by=Invoice.id,
                                 back_populates="customer")
# Base.metadata.create_all(engine)


# Declare session
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.orm import subqueryload

c1 = session.query(Customer).options(
    subqueryload(Customer.invoices)).filter_by(name='Ravi Kumar').one()

print(c1.name, c1.address, c1.email)

for x in c1.invoices:
   print("Invoice no : {}, Amount : {}".format(x.invno, x.amount))
