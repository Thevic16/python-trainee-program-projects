import re

if __name__ == '__main__':
    # Or operator |
    print(re.search(r"man|woman", "This man was here."))
    print(re.search(r"man|woman", "This woman was here."))

    # The Wildcard Character
    print(re.findall(r".at", "The cat in the hat sat here."))
    print(re.findall(r".at", "The bat went splat"))
    print(re.findall(r"...at", "The bat went splat"))

    # One or more non-whitespace that ends with 'at'
    print(re.findall(r'\S+at', "The bat went splat"))

    # Starts with and Ends With

    # Ends with a number
    print(re.findall(r'\d$', 'This ends with a number 2'))

    # Starts with a number
    print(re.findall(r'^\d', '1 is the loneliest number.'))

    # Exclusion
    phrase = "there are 3 numbers 34 inside 5 this sentence."
    print(re.findall(r'[^\d]', phrase))

    print(re.findall(r'[^\d]+', phrase))

    test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
    print(re.findall('[^!.? ]+', test_phrase))


