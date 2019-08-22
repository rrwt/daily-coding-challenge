"""
Suppose you have a multiplication table that is N by N. That is, a 2D array
where the value at the i-th row and j-th column is (i + 1) * (j + 1)
(if 0-indexed) or i * j (if 1-indexed).
Given integers N and X, write a function that returns the number of times X
appears as a value in an N by N multiplication table.
"""


def multi_count(n: int, x: int) -> int:
    """
    The count of number of factors (from 2 to n) is the count.
    exception: n > x, add 2 to the count (for 1 and x)

    Time Complexity: O(n)
    """

    if n < 1:
        return 0
    if x == 1:
        return 1

    total: int = 2 if x <= n else 0

    for i in range(2, n + 1):
        if x % i == 0:
            total += 1

    return total


if __name__ == "__main__":
    assert multi_count(1, 1) == 1
    assert multi_count(6, 12) == 4
    assert multi_count(2, 4) == 1
    assert multi_count(3, 6) == 2
    assert multi_count(6, 15) == 2
