import strawberry

from schemas.objects import Book, Author, User
from data.dataset import books, authors, users
from schemas.inputs import AddBookInput, AddAuthorInput, AddUserInput


@strawberry.type
class Mutation:
    @strawberry.field
    def add_book(self, book: AddBookInput) -> Book:
        new_book = Book(title=book.title, author=book.author)
        books.append(new_book)

        return new_book

    @strawberry.field
    def add_author(self, author: AddAuthorInput) -> Author:
        new_author = Author(name=author.name)
        authors.append(new_author)

        return new_author

    @strawberry.field
    def add_user(self, user: AddUserInput) -> User:
        new_user = User(username=user.username, password=user.password)
        users.append(new_user)

        return new_user
