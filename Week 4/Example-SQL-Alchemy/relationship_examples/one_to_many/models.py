# https://hackersandslackers.com/sqlalchemy-data-models/

"""Declare models and relationships."""
from sqlalchemy import create_engine, Boolean, Column, DateTime, Integer, \
    String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


engine = create_engine('sqlite:///blog.db', echo=True)
Base = declarative_base()


from sqlalchemy.orm import relationship


class User(Base):
    """User account."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    bio = Column(Text)
    avatar_url = Column(Text)
    role = Column(String(255))
    last_seen = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return "<User %r>" % self.username


class Comment(Base):
    """User-generated comment on a blog post."""

    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))  # Foreign key added
    post_id = Column(Integer, ForeignKey("post.id"), index=True)  # Foreign key added
    body = Column(Text)
    upvotes = Column(Integer, default=1)
    removed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    user = relationship("User")

    def __repr__(self):
        return "<Comment %r>" % self.id


class Post(Base):
    """Blog post/article."""

    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("user.id"))  # Foreign key added
    slug = Column(String(255), nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    summary = Column(String(400))
    feature_image = Column(String(300))
    body = Column(Text)
    status = Column(String(255), nullable=False, default="unpublished")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    # Relationships
    author = relationship("User", backref="posts")
    comments = relationship("Comment")

    def __repr__(self):
        return "<Post %r>" % self.slug


Base.metadata.create_all(engine)
