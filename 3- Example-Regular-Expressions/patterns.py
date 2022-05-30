import re

if __name__ == '__main__':
    text = "My telephone number is 408-555-1234"
    phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
    print(phone.group())

    # Quantifiers
    phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
    print(phone.group())

    # Groups
    phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    results = re.search(phone_pattern, text)

    # The entire result
    print(results.group())

    # Can then also call by group position.
    # remember groups were separated by parenthesis ()
    # Something to note is that group ordering starts at 1. Passing in 0
    # returns everything
    print(results.group(1))
    print(results.group(2))
    print(results.group(3))
