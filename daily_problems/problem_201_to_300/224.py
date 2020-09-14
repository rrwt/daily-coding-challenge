"""
Given a sorted array, find the smallest positive integer
that is not the sum of a subset of the array.
For example, for the input [1, 2, 3, 10], you should return 7.
"""
from typing import List


def smallest_positive_integer_not_in_array(arr: List[int]) -> int:
    """
    [1..N] can cover everything from 1 to (N * (N+1) / 2)
    """
    res = 1

    for num in arr:
        if num > res:
            return res
        else:
            res += num

    return res


if __name__ == "__main__":
    assert smallest_positive_integer_not_in_array([1, 2, 3, 10]) == 7
    assert smallest_positive_integer_not_in_array([1]) == 2
    assert smallest_positive_integer_not_in_array([2]) == 1
    assert smallest_positive_integer_not_in_array([1, 2, 3, 5, 15]) == 12
