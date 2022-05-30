# References
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/10-Python%20Decorators/01-Decorators.ipynb


# Scope Review

s = 'Global Variable'


def check_for_locals():
    print(locals())


'''
def hello(name='Jose'):
    return 'Hello ' + name
'''

# Functions within functions
'''
def hello(name='Jose'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")
'''

# Returning Functions
'''
def hello(name='Sam'):
    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome
'''


# Functions as Arguments
def hello():
    return 'Hi Jose!'


def other(func):
    print('Other code would go here')
    print(func())


# Creating a Decorator
def new_decorator(func):
    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")


if __name__ == '__main__':
    # Scope Review
    """
    check_for_locals()
    print(globals())
    print(globals().keys())
    print(globals()['s'])

    print(hello())
    greet = hello
    print(greet)
    print(greet())
    # del hello
    # hello()
    """

    # Functions within functions
    '''
    print(hello())
    '''

    # Returning Function
    '''
    x = hello()
    print(x)
    print(x())
    '''

    # Functions as Arguments
    # other(hello)

    # Creating a Decorator
    # print(func_needs_decorator())

    # Reassign func_needs_decorator
    # func_needs_decorator = new_decorator(func_needs_decorator)
    # print(func_needs_decorator())

    # Now let's understand how we can rewrite this code using the @ symbol.
    func_needs_decorator()
