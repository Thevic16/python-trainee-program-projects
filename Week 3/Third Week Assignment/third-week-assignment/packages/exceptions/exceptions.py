class IdDontExistException(Exception):
    """
    Exception throw when try to access an id that does not exist
    """
    def __init__(self, id):
        message = f'The id "{id}" do not exist.'
        super().__init__(message)


class TitleExistException(Exception):
    """
    Exception throw when try to assign a title that already exist
    """
    def __init__(self, title):
        message = f'The title "{title}" already exist.'
        super().__init__(message)
