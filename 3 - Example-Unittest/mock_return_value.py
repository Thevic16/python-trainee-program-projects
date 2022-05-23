# https://realpython.com/python-mock-library/#the-mock-object
from unittest.mock import Mock
import datetime

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)


def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)


if __name__ == '__main__':
    # Mock datetime to control today's date
    datetime = Mock()
    
    # Mock .today() to return Tuesday
    datetime.datetime.today.return_value = tuesday
    # Test Tuesday is a weekday
    assert is_weekday()
    # Mock .today() to return Saturday
    datetime.datetime.today.return_value = saturday
    # Test Saturday is not a weekday
    assert not is_weekday()
