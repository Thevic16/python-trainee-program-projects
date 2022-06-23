from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String

engine = create_engine('sqlite:///sales.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy.orm import relationship


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

Session = sessionmaker(bind=engine)
session = Session()

for c, i in session.query(Customer, Invoice).filter(
        Customer.id == Invoice.custid).all():
    print("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id, c.name,
                                                             i.invno,
                                                             i.amount))

print("\n\n The actual SQL JOIN syntax \n\n")
result = session.query(Customer).join(Invoice).filter(Invoice.amount == 100)
for row in result:
    for inv in row.invoices:
        print(row.id, row.name, inv.invno, inv.amount)
