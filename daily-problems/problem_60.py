"""
Given a multiset of integers,
return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into 
{15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
"""
from typing import Tuple


def split_arr(
    arr: list, l: int, index: int = 0, arr1: list = None, arr2: list = None
) -> Tuple[bool, list, list]:
    if index == l:
        return (True, arr1, arr2) if sum(arr1) == sum(arr2) else (False, arr1, arr2)
    else:
        if not arr1:
            arr1 = []
        if not arr2:
            arr2 = []

        res = split_arr(arr, l, index + 1, arr1 + [arr[index]], arr2)

        return (
            res
            if res[0] is True
            else split_arr(arr, l, index + 1, arr1, arr2 + [arr[index]])
        )


def can_split(arr: list) -> bool:
    if not arr:
        return True

    l: int = len(arr)

    if sum(arr) % 2 or l == 1:  # sum must be even
        return False

    res, arr1, arr2 = split_arr(arr, l)

    if res:
        print("The partitioned arrays for", arr, "are:", arr1, "and", arr2)

    return res


if __name__ == "__main__":
    s1, s2 = [15, 5, 20, 10, 35, 15, 10], [15, 5, 20, 10, 35]
    print("The array", s1, "can" if can_split(s1) else "cannot", "be split in two")
    print("The array", s2, "can" if can_split(s2) else "cannot", "be split in two")
