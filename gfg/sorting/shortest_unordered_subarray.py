"""Shortest Un-ordered Subarray
An array is given of n length, and problem is that we have to find the length
of shortest unordered {neither increasing nor decreasing} sub array in given array.
"""
from typing import Tuple
import random


def peak(arr: list, index: int) -> bool:
    return arr[index] > arr[index + 1] < arr[index + 2]


def trough(arr: list, index: int) -> bool:
    return arr[index] < arr[index + 1] > arr[index + 2]


def shortest_unordered_subarr(arr: list) -> Tuple[list, int]:
    """
    If there exists a solution, it would have inc then dec or vice versa structure.
    The length of the solution would always be 3.
    If we want to just find the length, we would just inquire if the condition satisfies
    and return 3 or 0
    """
    i = 0

    while i + 2 < len(arr):
        if peak(arr, i) or trough(arr, i):
            return arr[i : i + 3], 3
        i += 1

    return [], 0


if __name__ == "__main__":

    print("problem:", list(range(10)))
    print("solution:", shortest_unordered_subarr(list(range(10))))

    for _ in range(5):
        arr: list = [random.randint(1, 100) for _ in range(10)]
        print("problem:", arr)
        print("solution:", shortest_unordered_subarr(arr))
