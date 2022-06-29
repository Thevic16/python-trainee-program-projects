import typing
import strawberry


# Schema type
@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Author:
    name: str


@strawberry.type
class User:
    username: str
    password: str
