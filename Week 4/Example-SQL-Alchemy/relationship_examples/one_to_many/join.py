"""Perform JOIN queries on models with relationships."""
from sqlalchemy.orm import Session


from models import Post, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///blog.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()


def get_all_posts(session: Session, admin_user: User):
    """
    Fetch all posts belonging to an author user.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param admin_user: Author of blog posts.
    :type admin_user: User

    :return: None
    """
    posts = (
        session.query(Post)
        .join(User, Post.author_id == User.id)
        .filter_by(username=admin_user.username)
        .all()
    )
    for post in posts:
        post_record = {
            "post_id": post.id,
            "title": post.title,
            "summary": post.summary,
            "status": post.status,
            "feature_image": post.feature_image,
            "author": {
                "id": post.author_id,
                "username": post.author.username,
                "first_name": post.author.first_name,
                "last_name": post.author.last_name,
                "role": post.author.role,
            },
        }
        print(post_record)

admin_user = User(
    username="toddthebod",
    password="Password123lmao",
    email="todd@example.com",
    first_name="Todd",
    last_name="Birchard",
    bio="I write tutorials on the internet.",
    avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
    role="admin",
)

get_all_posts(session, admin_user)
