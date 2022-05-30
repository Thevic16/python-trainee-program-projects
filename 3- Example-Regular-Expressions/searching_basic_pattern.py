# Regular expressions: https://jovian.ai/galxy50/05-overview-of-regular-expressions
import re

if __name__ == '__main__':
    # Searching for Basic Patterns --------------------------------------------
    text = "The person's phone number is 408-555-1234. Call soon!"
    print('phone' in text)

    pattern = 'phone'
    match = re.search(pattern, text)
    print(match)
    print(match.span())
    print(match.start())
    print(match.end())

    pattern = 'NOT IN TEXT'
    print(re.search(pattern, text))

    # But what if the pattern occurs more than once?
    text = "my phone is a new phone"
    match = re.search("phone", text)
    print(match.span())

    # Notice it only matches the first instance. If we wanted a list of all
    # matches, we can use .findall() method:
    matches = re.findall("phone", text)
    print(matches)
    len(matches)

    # To get actual match objects, use the iterator:
    for match in re.finditer("phone", text):
        print(match.span())

    print(match.group())
