"""
Given an array of n positive integers and a number k. Find the minimum number
of swaps required to bring all the numbers less than or equal to k together.
"""


def min_swaps(arr: list, k: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    get the max count of elements less than or equal to k, which are together.
    The max swaps would be the total count - max count.
    """
    i, l, count_total, count_together = 0, len(arr), 0, 0

    while i < l:
        count_local: int = 0

        while i < l and arr[i] <= k:
            count_local += 1
            i += 1

        count_total += count_local
        count_together = max(count_together, count_local)
        i += 1

    return count_total - count_together


if __name__ == "__main__":
    assert min_swaps([2, 1, 5, 6, 3], 3) == 1
    assert min_swaps([2, 7, 9, 5, 8, 7, 4], 5) == 2
