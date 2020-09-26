"""
A fixed point in an array is an element whose value is equal to its index.
Given a sorted array of distinct elements, return a fixed point, if one
exists. Otherwise, return False.
For example,
    given [-6, 0, 2, 40], you should return 2.
    Given [1, 5, 7, 8], you should return False.
"""
from typing import List, Union


def fixed_point(array: List[int]) -> Union[int, bool]:
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) >> 1

        if mid == array[mid]:
            return mid
        elif mid < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == "__main__":
    assert fixed_point([-6, 0, 2, 40]) == 2
    assert fixed_point([1, 5, 7, 8]) is False
