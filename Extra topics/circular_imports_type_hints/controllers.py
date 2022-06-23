# https://adamj.eu/tech/2021/05/13/python-type-hints-how-to-fix-circular-imports/
# controllers.py
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Book


class BookController:
    def __init__(self, book: Book) -> None:
        self.book = book
