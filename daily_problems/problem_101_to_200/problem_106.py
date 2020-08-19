"""
Given an integer list where each number represents the number of hops you can make,
determine whether you can reach to the last index starting at index 0.
For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""
import sys
from typing import List


def can_reach_end(numbers: List[int]) -> bool:
    """
    Time Complexity: O(n)
    """
    max_reach = 0
    len_num = len(numbers)
    index = 0

    while index <= max_reach:
        max_reach = max(max_reach, index + numbers[index])

        if max_reach >= len_num - 1:
            return True

        index += 1

    return False


def min_num_steps_to_end(numbers: List[int]) -> int:
    """
    DP
    O(n*n) & O(n)
    """
    len_num = len(numbers)
    min_steps = [sys.maxsize] * len_num
    min_steps[0] = 0

    for index in range(1, len_num):
        for j in range(0, index):
            if j + numbers[j] >= index:
                min_steps[index] = min(min_steps[index], min_steps[j] + 1)

    return min_steps[-1] if min_steps[-1] != sys.maxsize else -1


if __name__ == "__main__":
    assert can_reach_end([2, 0, 1, 0]) is True
    assert can_reach_end([1, 1, 0, 1]) is False

    assert min_num_steps_to_end([2, 0, 1, 0]) == 2
    assert min_num_steps_to_end([1, 1, 0, 1]) == -1
