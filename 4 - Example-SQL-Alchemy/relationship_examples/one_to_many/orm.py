"""Create records related to one another via SQLAlchemy's ORM."""
from typing import Tuple

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from models import Post, User


def create_user(session: Session, user: User) -> User:
    """
    Create a new user if username isn't already taken.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param user: New user record to create.
    :type user: User

    :return: Optional[User]
    """
    try:
        existing_user = session.query(User).filter(
            User.username == user.username).first()
        if existing_user is None:
            session.add(user)  # Add the user
            session.commit()  # Commit the change
            print(f"Created user: {user}")
        else:
            print(f"Users already exists in database: {existing_user}")
        return session.query(User).filter(
            User.username == user.username).first()
    except IntegrityError as e:
        print(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        print(f"Unexpected error when creating user: {e}")
        raise e


def create_post(session: Session, post: Post) -> Post:
    """
    Create a post.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param post: Blog post to be created.
    :type post: Post

    :return: Post
    """
    try:
        existing_post = session.query(Post).filter(
            Post.slug == post.slug).first()
        if existing_post is None:
            session.add(post)  # Add the post
            session.commit()  # Commit the change
            print(
                f"Created post {post} published by user {post.author.username}"
            )
            return session.query(Post).filter(Post.slug == post.slug).first()
        else:
            print(f"Post already exists in database: {post}")
            return existing_post
    except IntegrityError as e:
        print(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        print(f"Unexpected error when creating user: {e}")
        raise e
