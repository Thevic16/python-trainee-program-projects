# Schema input
import strawberry


@strawberry.input
class AddBookInput:
    title: str = strawberry.field(description="The title of the book")
    author: str = strawberry.field(description="The name of the author")


@strawberry.input
class AddAuthorInput:
    name: str = strawberry.field(description="The name of the author")


@strawberry.input
class AddUserInput:
    username: str = strawberry.field(description="The name of the user")
    password: str = strawberry.field(description="The password of the user")