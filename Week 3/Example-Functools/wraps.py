from functools import wraps


def f(x):
    """f's Docstring"""
    return x


@wraps(f)
def z(x):
    return x * x


if __name__ == '__main__':
    print('f name :', f.__name__)
    print('Documentation of f :', f.__doc__)
    
    print('f name :', z.__name__)
    print('Documentation of f :', z.__doc__)
