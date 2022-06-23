# Referencia: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/11-Python%20Generators/01-Iterators%20and%20Generators.ipynb

# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num ** 3


def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# next() and iter() built-in functions
def simple_gen():
    for x in range(3):
        yield x


if __name__ == '__main__':
    # Generator function for the cube of numbers (power of 3)
    '''
    for x in gencubes(10):
        print(x)
    '''

    # fibonacci numbers
    print('Fibonacci numbers')
    for num in genfibon(10):
        print(num)

    # next() and iter() built-in functions
    # Assign simple_gen
    g = simple_gen()

    print('Assign simple_gen')
    print(next(g))
    print(next(g))
    print(next(g))

    '''
    Interesting, this means that a string object supports iteration,
     but we can not directly iterate over it as we could with a generator
      function. The iter() function allows us to do just that!
    '''
    s = 'hello'
    s_iter = iter(s)
    print(next(s_iter))
    print(next(s_iter))
