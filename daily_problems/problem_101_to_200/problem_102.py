"""
Given a list of integers and a number K,
return which contiguous elements of the list sum to K.

For example,
    if the list is [1, 2, 3, 4, 5] and K is 9,
    then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""
from typing import List


def contiguous_sum(numbers: List[int], k: int) -> List[int]:
    """
    Only works for +ve values
    O(n)
    """
    start, found = 0, False
    total = numbers[0]

    for index, value in enumerate(numbers[1:], start=1):
        cur_total = total + value

        if cur_total <= k:
            total = cur_total
        else:
            total = cur_total - numbers[start]
            start += 1

        if total == k:
            return numbers[start: index + 1]

    return []


if __name__ == "__main__":
    assert contiguous_sum([1, 2, 3, 4, 5], 9) == [2, 3, 4]
