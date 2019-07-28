"""
Given an array of n positive integers. We are required to write a program to print the
minimum product of k integers of the given array.
"""
import heapq
import operator
from functools import reduce


def min_product(arr: list, k: int) -> int:
    """
    Min heap can be used to one by one pop and multiply items
    """
    heapq.heapify(arr)
    return reduce(operator.mul, heapq.nsmallest(k, arr), 1)


if __name__ == "__main__":
    print(min_product([198, 76, 544, 123, 154, 675], 2))
    print(min_product([11, 8, 5, 7, 5, 100], 4))
