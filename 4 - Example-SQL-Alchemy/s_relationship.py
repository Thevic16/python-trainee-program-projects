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

# Insert customers ------------------------------------------------------------
'''
session.add_all([
    Customer(name='Komal Pande', address='Koti, Hyderabad',
             email='komal@gmail.com'),
    Customer(name='Rajender Nath', address='Sector 40, Gurgaon',
             email='nath@gmail.com'),
    Customer(name='S.M.Krishna', address='Budhwar Peth, Pune',
             email='smk@gmail.com')]
)
'''

# Insert invoices -------------------------------------------------------------
'''
session.add_all([
    Invoice(custid=1, invno=1, amount=10),
    Invoice(custid=1, invno=2, amount=100),
    Invoice(custid=2, invno=2, amount=77),
    Invoice(custid=3, invno=3, amount=88),
    Invoice(custid=4, invno=74, amount=99),
    Invoice(custid=4, invno=56, amount=67),
    Invoice(custid=4, invno=62, amount=500), ]
)
'''

# session.commit()

# Query customers -------------------------------------------------------------
print('\n\n Query customers \n\n')
result = session.query(Customer).all()
for row in result:
    print("ID:", row.id, "Name: ", row.name, "Address:", row.address, "Email:",
          row.email)

# Query invoices --------------------------------------------------------------
print('\n\n Query invoices \n\n')
result = session.query(Invoice).all()
for row in result:
    print("ID:", row.id, "custid: ", row.custid, "invno:", row.invno,
          "amount:", row.amount)


