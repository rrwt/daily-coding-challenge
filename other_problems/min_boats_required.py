"""
Given N people need to be rescued by crossing the river by boat.
Each boat can carry a maximum weight of given limit K.
Each boat carries at most 2 people at the same time,
provided the sum of the weight of those people is at most limit K.
"""
from typing import List


def min_boats(weights: List[int], limit: int) -> int:
    weights.sort()
    last_index = len(weights) - 1
    first_index = 0
    count = 0

    while last_index >= first_index:
        if first_index == last_index and weights[first_index] <= limit:
            first_index += 1
        elif weights[last_index] + weights[first_index] <= limit:
            first_index += 1
            last_index -= 1
        elif weights[last_index] <= limit:
            last_index -= 1
        else:
            return -1
        count += 1

    return count


if __name__ == "__main__":
    assert min_boats([1, 2], 3) == 1
    assert min_boats([5, 1, 4, 2], 6) == 2
    assert min_boats([3, 4, 1, 2], 4) == 3
