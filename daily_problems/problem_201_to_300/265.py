"""
MegaCorp wants to give bonuses to its employees based on
how many lines of codes they have written. They would like
to give the smallest positive amount to each worker consistent
with the constraint that if a developer has written more lines
of code than their neighbor, they should receive more money.
Given an array representing a line of seats of employees at
MegaCorp, determine how much each one should get paid.
For example, given [10, 40, 200, 1000, 60, 30],
    you should return [1, 2, 3, 4, 2, 1].
"""
from typing import List


def adjust_neighbors(
    loc: List[int], res: List[int], index: int, start: int
) -> List[int]:
    res[index] = 1

    for j in range(index - 1, start - 1, -1):
        if loc[j] > loc[j + 1] and res[j] <= res[j + 1]:
            res[j] = res[j + 1] + 1
        elif loc[j] < loc[j + 1] and res[j] >= res[j + 1]:
            res[j] = res[j + 1] - 1
        elif loc[j] == loc[j+1] and res[j] != res[j + 1]:
            res[j] = res[j + 1]
        else:
            break

    return res


def smallest_bonus(loc: List[int]) -> List[int]:
    size = len(loc)
    res = [0] * size
    res[0] = 1

    for index in range(1, size):
        if loc[index] > loc[index - 1]:
            res[index] = res[index - 1] + 1
        elif loc[index] < loc[index - 1]:
            res[index] = min(res[index - 1] - 1, 1)
        else:
            res[index] = res[index - 1]

    min_val = 1
    start = 0
    for index in range(1, size):
        if res[index] < 1:
            if res[index] < min_val:
                min_val = res[index]
                res = adjust_neighbors(loc, res, index, 0)
            else:
                res = adjust_neighbors(loc, res, index, start)

            start = index

    return res


if __name__ == "__main__":
    assert smallest_bonus([10, 40, 200, 1000, 60, 30]) == [1, 2, 3, 4, 2, 1]
    assert smallest_bonus([10, 40, 200, 1000, 900, 800, 30]) == [1, 2, 3, 4, 3, 2, 1]
    assert smallest_bonus(
        [10, 40, 80, 40, 50, 60, 70, 80, 90, 30, 20, 10]
    ) == [1, 2, 3, 1, 2, 3, 4, 5, 6, 3, 2, 1]
