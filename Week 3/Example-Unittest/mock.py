# https://realpython.com/python-mock-library/#the-mock-object
from unittest.mock import Mock


if __name__ == '__main__':
    mock = Mock()
    print(mock)

    # Lazy Attributes and Methods
    print(mock.some_attribute)
    print(mock.do_something())

    json = Mock()
    print(json.loads('{"k": "v"}').get('k'))
