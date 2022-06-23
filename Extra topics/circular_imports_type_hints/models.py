# https://adamj.eu/tech/2021/05/13/python-type-hints-how-to-fix-circular-imports/
# models.py
from controllers import BookController


class Book:

    def get_controller(self) -> BookController:
        return BookController(self)
