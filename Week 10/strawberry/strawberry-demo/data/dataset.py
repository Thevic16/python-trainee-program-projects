from typing import List

from schemas.objects import Book, Author, User

books: List[Book] = []
authors: List[Author] = []
users: List[User] = []


def get_books():
    return books


def get_authors():
    return authors


def get_users():
    return users
