"""
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order
is an array representing whether each number is larger or smaller than the last.
Given this information, reconstruct an array that is consistent with it.
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4]
"""
from typing import List


def reconstruct(nums: List[str]) -> List[int]:
    """
    Let's assume first number to be 0.
    Let's set max_num = min_num = 0.
    Everytime we encounter a +, we increment max_num and append it.
    Everytime we encounter a -, we decrement min_num and append it.
    Finally, iterate over the list again and add min_num to all.
    """
    max_num = min_num = 0
    size = len(nums)
    res = [0] * size

    for index in range(1, size):
        if nums[index] == "+":
            max_num += 1
            res[index] = max_num
        if nums[index] == "-":
            min_num -= 1
            res[index] = min_num

    return [num - min_num for num in res]


if __name__ == "__main__":
    assert reconstruct([None, "+", "+", "-", "+"]) == [1, 2, 3, 0, 4]
    assert reconstruct([None, "-", "-", "-", "+"]) == [3, 2, 1, 0, 4]
    assert reconstruct([None, "+", "+", "+", "+"]) == [0, 1, 2, 3, 4]
    assert reconstruct([None, "-", "-", "-", "-"]) == [4, 3, 2, 1, 0]
