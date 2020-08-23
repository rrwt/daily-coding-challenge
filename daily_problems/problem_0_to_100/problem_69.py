"""
Given a list of integers, return the largest product
that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2],
we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""
import sys
from functools import reduce
from operator import mul


def largest_product_naive(arr: list) -> int:
    """
    Time Complexity: O(n*n*n)
    """
    max_product: int = -sys.maxsize
    length: int = len(arr)

    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                max_product = max(max_product, arr[i] * arr[j] * arr[k])

    return max_product


def largest_product(arr: list) -> int:
    """
    Time Complexity: O(n*log(n))
    """
    k = len(arr) - 1

    if k < 3:
        return reduce(mul, arr)

    arr.sort()
    return max(arr[k] * arr[0] * arr[1], arr[k] * arr[k - 1] * arr[k - 2])


if __name__ == "__main__":
    arr_list: list = [[-10, -10, 5, 2], [-10, 10, 5, 2], [-2, -3, 4, 6], [1, 2, 3, 4]]

    for arr in arr_list:
        print(arr, largest_product_naive(arr), sep=" -> ")
        print(arr, largest_product(arr), sep=" -> ")
