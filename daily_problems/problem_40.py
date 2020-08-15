"""
Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example,
    given [6, 1, 3, 3, 3, 6, 6], return 1.
    Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
from array import array
from collections import defaultdict


def find_unique(arr: array) -> int:
    """
    Hash Table
    O(n) & O(n)
    """
    hash_map = defaultdict(int)

    for _ in arr:
        hash_map[_] += 1

    for key, value in hash_map.items():
        if value == 1:
            return key

    return -1


def find_unique_opt(arr: array) -> int:
    """
    Bitwise add and mod 3
    O(n) & O(1)
    """
    res = 0

    for i in range(32):  # 32 bit integer
        cur_sum = 0
        multiplier = 1 << i

        for val in arr:
            cur_sum += multiplier & val

        res |= multiplier if cur_sum % 3 else 0

    return res


if __name__ == "__main__":
    assert find_unique(array("I", [6, 1, 3, 3, 3, 6, 6])) == 1
    assert find_unique(array("I", [13, 19, 13, 13])) == 19
    assert find_unique_opt(array("I", [6, 1, 3, 3, 3, 6, 6])) == 1
    assert find_unique_opt(array("I", [13, 19, 13, 13])) == 19
