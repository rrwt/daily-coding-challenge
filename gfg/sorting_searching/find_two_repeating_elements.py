"""
You are given an array of n+2 elements. All elements of the array are in range 1 to n.
And all elements occur once except two numbers which occur twice. Find the two repeating numbers.
"""
from typing import Tuple


def repeating(arr: list) -> Tuple[int, int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    xor = 0

    for elem in arr:
        xor ^= elem

    for i in range(1, len(arr) - 1):
        xor ^= i

    set_bit = xor & -xor
    x, y = 0, 0

    for elem in arr:
        if elem & set_bit:
            x ^= elem
        else:
            y ^= elem

    for i in range(1, len(arr) - 1):
        if i & set_bit:
            x ^= i
        else:
            y ^= i

    return x, y


if __name__ == "__main__":
    print(repeating([4, 2, 4, 5, 2, 3, 1]))
