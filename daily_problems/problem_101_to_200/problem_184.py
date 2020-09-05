"""
Given n numbers, find the greatest common denominator between them.
For example, given the numbers [42, 56, 14], return 14.
"""
from typing import List


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b

    return gcd(b % a, a)


def mul_gcd(nums: List[int]) -> int:
    res = nums[0]

    for num_2 in nums[1:]:
        res = gcd(res, num_2)

    return res


if __name__ == "__main__":
    print(mul_gcd([42, 56, 14]))
