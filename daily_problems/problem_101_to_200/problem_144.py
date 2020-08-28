"""
Given an array of numbers and an index i, return the index of the nearest larger number
of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
If two distances to larger numbers are the equal, then return any one of them.
If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""
from typing import List, Optional


def nearest_larger_number(numbers: List[int], index: int) -> Optional[int]:
    """
    Time Complexity: O(n)
    Space Complexity: (1)
    TODO: Follow up
    """
    val = numbers[index]
    size = len(numbers)

    for diff in range(1, size):
        if index + diff < size and numbers[index + diff] > val:
            return numbers[index + diff]
        if index - diff > -1 and numbers[index - diff] > val:
            return numbers[index - diff]

    return None


if __name__ == "__main__":
    assert nearest_larger_number([4, 1, 3, 5, 6], 0) == 5
