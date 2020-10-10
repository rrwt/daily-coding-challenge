"""
An imminent hurricane threatens the coastal town of Codeville.
If at most two people can fit in a rescue boat, and the maximum
weight limit for a given boat is k, determine how many boats will
be needed to save everyone.
For example,
    given a population with weights [100, 200, 150, 80] and a boat
    limit of 200, the smallest number of boats required will be three.
"""
from typing import List


def min_boats(weights: List[int], max_weight: int) -> int:
    weights.sort(reverse=True)

    start, end = 0, len(weights) - 1
    num_boats = 0

    while end > start:
        if weights[end] + weights[start] <= max_weight:
            end -= 1
            start -= 1
        elif weights[end] <= max_weight:
            end -= 1
        else:
            raise ValueError("Weight cannot be carried in a boat")

        num_boats += 1

    return num_boats


if __name__ == "__main__":
    assert min_boats([100, 200, 150, 80], 200) == 3
