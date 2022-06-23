from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print([factorial(n) for n in range(7)])
    print(factorial.cache_info())
    
