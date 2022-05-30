# Reference: https://www.geeksforgeeks.org/functools-module-in-python/

from functools import reduce

if __name__ == '__main__':
    list1 = [2, 4, 7, 9, 1, 3]
    sum_of_list1 = reduce(lambda a, b: a + b, list1)

    list2 = ["abc", "xyz", "def"]
    max_of_list2 = reduce(lambda a, b: a if a > b else b, list2)

    print('Sum of list1 :', sum_of_list1)
    print('Maximum of list2 :', max_of_list2)
