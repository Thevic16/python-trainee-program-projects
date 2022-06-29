# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/07-args%20and%20kwargs.ipynb

def myfunc(a, b):
    return sum((a, b)) * .05


print(myfunc(40, 60))


def myfunc(a=0, b=0, c=0, d=0, e=0):
    return sum((a, b, c, d, e)) * .05


print(myfunc(40, 60, 20))

# *args
'''
When a function parameter starts with an asterisk, it allows for an arbitrary
 number of arguments, and the function takes them in as a tuple of values.
'''


def myfunc(*args):
    return sum(args) * .05


print(myfunc(40, 60, 20))


# **kwargs
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(
            f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")


print(myfunc(fruit='pineapple'))
print(myfunc())

# *args and **kwargs combined
"""
You can pass *args and **kwargs into the same function, but *args have to
 appear before **kwargs
"""


def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(
            f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc('eggs', 'spam', fruit='cherries', juice='orange')
