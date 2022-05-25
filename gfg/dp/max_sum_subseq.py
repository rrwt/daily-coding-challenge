"""Maximum sum increasing subsequence

Given an array of n positive integers. Write a program to find
the sum of maximum sum subsequence of the given array such that
the integers in the subsequence are sorted in increasing order.
"""


def max_sum_naive(arr: list, length: int, index: int, prev_max: int) -> int:
    """
    We can either take or leave the current number depending on previous max number
    """
    if index >= length:
        return 0

    cur_max = 0
    if arr[index] > prev_max:
        cur_max = arr[index] + max_sum_naive(arr, length, index + 1, arr[index])

    return max(cur_max, max_sum_naive(arr, length, index + 1, prev_max))


def max_sum_tabulated(arr: list) -> int:
    length: int = len(arr)
    result: list = [0] * length

    for i in range(length):
        result[i] = arr[i]

    for i in range(1, length):
        for j in range(i):
            if arr[i] > arr[j]:
                result[i] = max(result[i], result[j] + arr[i])

    return max(result)


if __name__ == "__main__":
    arr: list = [1, 101, 2, 3, 100, 4, 5]
    arr2: list = [3, 4, 5, 10]

    assert max_sum_naive(arr, len(arr), 0, 0) == 106
    assert max_sum_naive(arr2, len(arr2), 0, 0) == 22

    assert max_sum_tabulated(arr) == 106
    assert max_sum_tabulated(arr2) == 22
