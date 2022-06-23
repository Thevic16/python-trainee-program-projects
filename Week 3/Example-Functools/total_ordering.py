# Reference: https://www.geeksforgeeks.org/functools-module-in-python/

from functools import total_ordering


@total_ordering
class N:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    # Reverse the function of
    # '<' operator and accordingly
    # other rich comparison operators
    # due to total_ordering decorator
    def __lt__(self, other):
        return self.value < other.value


if __name__ == '__main__':
    print('6 > 2 :', N(6) > N(2))
    print('3 < 1 :', N(3) < N(1))
    print('2 <= 7 :', N(2) <= N(7))
    print('9 >= 10 :', N(9) >= N(10))
    print('5 == 5 :', N(5) == N(5))
