"""
Given an array of integers, find the maximum XOR of any two elements.
"""
from typing import List


def max_xor(nums: List[int]) -> int:
    size = len(nums)
    max_val = 0

    for i in range(size - 1):
        for j in range(i + 1, size):
            max_val = max(max_val, nums[i] ^ nums[j])

    return max_val


if __name__ == "__main__":
    print(max_xor(list(range(10))))
