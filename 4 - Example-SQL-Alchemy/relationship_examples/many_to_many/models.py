from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, \
    func, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('team_id', Integer, ForeignKey('example.sqlalchemy_tutorial_players.team_id')),
    Column('id', Integer, ForeignKey('example.sqlalchemy_tutorial_teams.id'))
)


class Player(Base):
    """Individual player belonging to a team."""

    __tablename__ = "player"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    team_id = Column(Integer, ForeignKey("team.id"), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    position = Column(String(100), nullable=False)
    injured = Column(Boolean)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    team = relationship("Team")

    def __repr__(self):
        return "<Player {}>".format(self.id)


class Team(Base):
    """Team consisting of many players."""

    __tablename__ = "team"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return "<Team {}>".format(self.id)