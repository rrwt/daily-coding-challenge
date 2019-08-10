"""
Given an array of positive numbers, find the maximum sum of a subsequence with the
constraint that no 2 numbers in the sequence should be adjacent in the array.
So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15
(sum of 3, 5 and 7).Answer the question in most efficient way.
"""


def max_sum(arr: list) -> int:
    """
    Time Complexity: O(n)
    """
    l: int = len(arr)
    res: int = 0

    if l == 0:
        res = 0
    elif l == 1:
        res = arr[0]
    else:
        sum_inc: int = arr[1]
        sum_exc: int = arr[0]

        for i in range(2, l):
            sum_inc, sum_exc = sum_exc + arr[i], max(sum_exc, sum_inc)

        res = max(sum_exc, sum_inc)

    return res


if __name__ == "__main__":
    assert max_sum([]) == 0
    assert max_sum([5]) == 5
    assert max_sum([7, 15]) == 15
    assert max_sum([5, 8, 5]) == 10
    assert max_sum([5, 18, 5]) == 18
    assert max_sum([1, 2, 3, 4]) == 6
    assert max_sum([2, 1, 3, 4]) == 6
