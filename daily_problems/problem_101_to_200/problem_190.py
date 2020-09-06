"""
Given a circular array, compute its maximum subarray sum in O(n) time.
A subarray can be empty, and in this case the sum is 0.
For example,
    given [8, -1, 3, 4], return 15 as we choose the numbers
    3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""
from typing import List


def kadane_sum(arr: List[int]) -> int:
    max_sum = 0
    cur_sum = 0

    for element in arr:
        if element + cur_sum > 0:
            cur_sum += element
        else:
            cur_sum = 0

        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum


def subarray_sum(arr: List[int]) -> int:
    """
    Kadane's algorithm only works with non circular arrays.
    Two Cases Arise:
        1. Max sum subarray is does not contain circular elements.
            In this case, we use normal kadane's algorithm
        2. It is a circular subarray.
            We change the sign of each element, calculate the max sum,
            and subtract it from total sum.
    """
    total = sum(arr)
    max_kadane = kadane_sum(arr)
    max_negative_kadane = kadane_sum([-x for x in arr])
    return max(max_kadane, total + max_negative_kadane)


if __name__ == "__main__":
    assert subarray_sum([8, -1, 3, 4]) == 15
    assert subarray_sum([-4, 5, 1, 0]) == 6
    assert subarray_sum([-4, 5, 1, -1]) == 6
    assert subarray_sum([10, -4, -3, 5, 1, -7, 5, -4, 10]) == 21
