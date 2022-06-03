# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_building_relationship.htm
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


# __eq__() --------------------------------------------------------------------
print('\n\n __eq__() \n\n')
result = session.query(Customer).join(Invoice).filter(Invoice.invno.__eq__(1))
for row in result:
    print("ID:", row.id, "Name: ", row.name, "Address:", row.address, "Email:",
          row.email)

# __ne__() --------------------------------------------------------------------
print('\n\n __ne__() \n\n')
result = session.query(Customer).join(Invoice).filter(Invoice.invno.__ne__(3))
for row in result:
    print("ID:", row.id, "Name: ", row.name, "Address:", row.address, "Email:",
          row.email)

# contains() ------------------------------------------------------------------
'''
print('\n\n contains() \n\n')
result = session.query(Invoice).filter(Invoice.invno.contains([3,4,5]))
for row in result:
    print("ID:", row.id, "custid: ", row.custid, "invno:", row.invno,
          "amount:", row.amount)
'''

# any() -----------------------------------------------------------------------
print('\n\n __ne__() \n\n')
result = session.query(Customer).filter(Customer.invoices.any(
    Invoice.invno==1))
for row in result:
    print("ID:", row.id, "Name: ", row.name, "Address:", row.address, "Email:",
          row.email)

# has() ------------------------------------------------------------------
print('\n\n has() \n\n')
result = session.query(Invoice).filter(Invoice.customer.has(
    name = 'Ravi Kumar'))
for row in result:
    print("ID:", row.id, "custid: ", row.custid, "invno:", row.invno,
          "amount:", row.amount)

