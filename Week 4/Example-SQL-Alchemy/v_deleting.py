# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_deleting_related_objects.htm
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, \
    MetaData

engine = create_engine('sqlite:///sales.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy.orm import relationship

meta = MetaData()


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
                                 back_populates="customer",
                                 cascade="all,delete, delete-orphan")
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

c1 = Customer(name='Ravi Kumar', address='Station Road Nanded',
              email='ravi@gmail.com')
session.add(c1)

i1 = Invoice(custid=1, invno=1, amount=1)
session.add(i1)

i2 = Invoice(custid=1, invno=2, amount=1)
session.add(i2)

session.commit()

# Deleting
x = session.query(Customer).get(1)
session.delete(x)
print(session.query(Customer).filter_by(id=1).count())
print(session.query(Invoice).filter(Invoice.invno.in_([1, 2])).count())
