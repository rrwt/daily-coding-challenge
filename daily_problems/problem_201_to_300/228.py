"""
Given a list of numbers, create an algorithm that arranges
them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
"""
from collections import defaultdict
from functools import cmp_to_key
from typing import List


def get_sorted(num_1: str, num_2: str) -> int:
    len_1 = len(num_1)
    len_2 = len(num_2)

    if len_1 < len_2:
        num_1 += num_1[-1] * (len_2 - len_1)
    elif len_2 < len_1:
        num_2 += num_2[-1] * (len_1 - len_2)

    for char_1, char_2 in zip(num_1, num_2):
        if char_1 < char_2:
            return -1
        elif char_2 < char_1:
            return 1


def largest_integer(nums: List[int]) -> str:
    str_nums = defaultdict(list)

    for index, num in enumerate(nums):
        str_num = str(num)
        str_nums[int(str_num[0])].append(str_num)

    val = ""

    for key in sorted(str_nums.keys(), reverse=True):
        val += "".join(sorted(str_nums[key], key=cmp_to_key(get_sorted), reverse=True))

    return val


if __name__ == "__main__":
    assert largest_integer([10, 7, 76, 415]) == "77641510"
    assert largest_integer([1, 34, 3, 98, 9, 76, 45, 4, 12, 121]) == "99876454343121211"
