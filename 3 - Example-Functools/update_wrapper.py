from functools import update_wrapper, partial


def power(a, b):
    """a to power b"""
    return a**b


if __name__ == '__main__':
    # partial fuction
    pow2 = partial(power, b = 2)
    pow2.__doc__= """a to power 2"""
    pow2.__name__= 'pow2'

    print('Before wrapper update -')
    print('Documentation of pow2: ', pow2.__doc__)
    print('Name of pw2 :', pow2.__name__)
    print()
    update_wrapper(pow2, power)
    print('After wrapper update -')
    print('Documentation of pow2 :', pow2.__doc__)
    print('Name of pow2 :', pow2.__name__)
