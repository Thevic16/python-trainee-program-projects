from models import Post, User
from relationship_examples.one_to_many.orm import create_user, create_post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///blog.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()


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

# Create admin user & two posts
admin_user = create_user(session, admin_user)

post_1 = Post(
    author_id=admin_user.id,
    slug="fake-post-slug",
    title="Fake Post Title",
    status="published",
    summary="A fake post to have some fake comments.",
    feature_image="https://cdn.hackersandslackers.com/2021/01/logo-smaller@2x.png",
    body="Cheese slices monterey jack cauliflower cheese dolcelatte cheese and wine fromage frais rubber cheese gouda. Rubber cheese cheese and wine cheeseburger cheesy grin paneer paneer taleggio caerphilly.  Edam mozzarella.",
)

post_1 = create_post(session, post_1)

post_2 = Post(
    author_id=admin_user.id,
    slug="an-additional-post",
    title="Yet Another Post Title",
    status="published",
    summary="An in-depth exploration into writing your second blog post.",
    feature_image="https://cdn.hackersandslackers.com/2021/01/logo-smaller@2x.png",
    body="Smelly cheese cheese slices fromage. Pepper jack taleggio monterey jack cheeseburger pepper jack swiss everyone loves. Cheeseburger say cheese brie fromage frais swiss when the cheese comes out everybody's happy babybel cheddar. Cheese and wine cheesy grin",
)

post_2 = create_post(session, post_2)

print(post_1.author.email)
print(admin_user.posts)
