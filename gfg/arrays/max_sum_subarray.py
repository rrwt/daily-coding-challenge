"""
An array is given, find length of the subarray having maximum sum.
"""


def max_sum_subarray(arr: list) -> int:
    max_sum, curr_max, curr_start, start, end = 0, 0, 0, -1, 0

    for index, el in enumerate(arr):
        curr_max += el

        if curr_max > max_sum:
            start = curr_start
            end = index
            max_sum = curr_max

        if curr_max < 0:
            curr_max = 0
            curr_start = index + 1

    return end - start + 1 if end >= start >= 0 else -1


if __name__ == "__main__":
    assert max_sum_subarray([1, -2, 1, 1, -2, 1]) == 2
    assert max_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3]) == 5
