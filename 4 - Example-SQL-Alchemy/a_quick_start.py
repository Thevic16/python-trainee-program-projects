# https://docs.sqlalchemy.org/en/14/orm/quickstart.html#simple-select

from sqlalchemy import Column, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user",
                             cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}," \
               f" fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# Create an Engine
engine = create_engine("sqlite://", echo=True, future=True)

# Base.metadata.create_all(engine)
'''
Using our table metadata and our engine, we can generate our schema at once in
 our target SQLite database, using a method called MetaData.create_all():
'''
Base.metadata.create_all(engine)

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )

    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )

    patrick = User(name="patrick", fullname="Patrick Star")

    session.add_all([spongebob, sandy, patrick])
    session.commit()

    # Simple SELECT
    print(" \n\n # Simple SELECT \n\n")
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

    for user in session.scalars(stmt):
        print(user)

    # SELECT with JOIN
    print(" \n\n # SELECT with JOIN \n\n")
    stmt = (
        select(Address).join(Address.user).where(User.name == "sandy").where(
            Address.email_address == "sandy@sqlalchemy.org")
    )
    sandy_address = session.scalars(stmt).one()
    print(sandy_address)

    # Make Changes
    print(" \n\n Make Changes \n\n")
    sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"
    session.commit()

    # Some Deletes
    print(" \n\n Some Deletes \n\n")
    sandy = session.get(User, 2)
    sandy.addresses.remove(sandy_address)
    """
        We can choose to emit the DELETE SQL for what’s set to be changed so
         far, without committing the transaction, using the Session.flush()
          method.
    """
    session.flush()

    session.delete(patrick)
    session.commit()
