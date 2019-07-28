"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0,
since we would not take any elements.

Do this in O(N) time.
"""
import sys
from copy import deepcopy
from typing import Tuple


def max_sum(arr: list) -> Tuple[list, int]:
    """
    Inc array and value considers current maximum.
    Exc array and value considers historical maximum.
    Time Complexity: O(n)
    Space Complexity: O(1)
    Note: Extra time is taken to copy the inc array into exc array
    """

    sum_inc, sum_exc = -sys.maxsize, -sys.maxsize
    arr_inc: list = []
    arr_exc: list = []
    index = 0

    while index < len(arr):
        el = arr[index]

        if el > el + sum_inc:
            sum_inc = el
            arr_inc = [el]
        else:
            sum_inc = el + sum_inc
            arr_inc.append(el)

        if sum_inc > sum_exc:
            sum_exc = sum_inc
            arr_exc = deepcopy(arr_inc)
        index += 1

    if sum_inc > 0 and sum_inc >= sum_exc:
        return arr_inc, sum_inc
    elif sum_exc > 0 and sum_exc > sum_inc:
        return arr_exc, sum_exc
    else:
        return [], 0


if __name__ == "__main__":
    for arr in [[34, -50, 42, 14, -5, 86], [-5, -1, -8, -9]]:
        print("maximum sum subarray and sum for array", arr, "are", max_sum(arr))
