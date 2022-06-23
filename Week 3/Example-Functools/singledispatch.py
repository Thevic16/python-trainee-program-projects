from functools import singledispatch


@singledispatch
def fun(s):
    print(s)


@fun.register(int)
def _(s):
    print(s * 2)


if __name__ == '__main__':
    fun('GeeksforGeeks')
    fun(10)
