"""
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
If there are multiple smallest sets, return any of them.

For example,
    given the intervals [0, 3], [2, 6], [3, 4], [6, 9],
    one set of numbers that covers all these intervals is {3, 6}.
"""
from copy import deepcopy
from typing import List


def cover_intervals(numbers: List[List[int]]) -> List[int]:
    # alt question: https://www.dailycodingproblem.com/blog/smallest-interval-of-k-sorted-lists/
    # TODO: Optimize

    # sort the numbers by first number.
    numbers = sorted(numbers, key=lambda num: num[0])
    results = [[numbers[0][1]]]

    for index, (first, second) in enumerate(numbers[1:], start=1):
        temp_res = None

        for ind, res in enumerate(results):
            # consider all intervals
            if res[-1] < first:
                if temp_res is None:
                    temp_res = deepcopy(results)

                temp_res[ind] = res + [first]
                temp_res.append(res + [second])

        if temp_res:
            results = temp_res

    min_len = len(results[0])
    index = 0

    for ind, res in enumerate(results[1:], start=1):
        cur_len = len(res)

        if cur_len < min_len:
            min_len = cur_len
            index = ind

    return results[index]


if __name__ == "__main__":
    assert cover_intervals([[0, 3], [2, 6], [3, 4], [6, 9]]) in ([3, 6], [3, 9])
    assert cover_intervals([[10, 20], [-20, 10]]) == [10]
    assert cover_intervals([[0, 3]]) in ([0], [3])
    assert cover_intervals([[0, 3], [2, 6]]) == [3]
    assert cover_intervals([[0, 3], [10, 20], [15, 40], [25, 30]]) in ([3, 20, 25], [3, 10, 40])
