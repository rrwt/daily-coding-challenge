"""
Given a sorted list of integers of length N, determine
if an element x is in the list without performing
any multiplication, division, or bit-shift operations.
"""
from bisect import bisect
from typing import List


def is_in_list(lst: List[int], el: int) -> bool:
    pos = bisect(lst, el)
    return pos >= 0 and lst[pos - 1] == el


if __name__ == "__main__":
    assert is_in_list([1, 2, 3, 4, 5], 3) is True
    assert is_in_list([10, 20, 30, 40, 50], 5) is False
    assert is_in_list([1, 2, 3, 4, 5], 6) is False
