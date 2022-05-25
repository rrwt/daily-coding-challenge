# You are given a bag of size W kg, and you are provided costs of packets different weights
# of oranges in array cost[] where cost[i] is basically cost of ‘i’ kg packet of oranges.
# Where cost[i] = -1 means that ‘i’ kg packet of orange is unavailable
# Find the minimum total cost to buy exactly W kg oranges and if it is not possible
# to buy exactly W kg oranges then print -1. It may be assumed that there is infinite
# supply of all available packet types.
from typing import List
import sys


def min_cost(costs: List[int], weight: int) -> int:
    # O(n*k)
    weights = [sys.maxsize] * (weight + 1)
    weights[0] = 0

    for i in range(1, weight+1):
        min_wt = sys.maxsize

        for j in range(0, (min(i, (len(costs) + 1) // 2))):
            if costs[j] > -1:
                min_wt = min(min_wt, costs[j] + weights[i - j - 1])

        weights[i] = min_wt

    return weights[-1] if weights[-1] < sys.maxsize else -1


if __name__ == "__main__":
    assert min_cost([20, 10, 4, 50, 100], 5) == 14
    assert min_cost([1, 10, 4, 50, 100], 5) == 5
    assert min_cost([1, 2, 3, 4, 5], 5) == 5
    assert min_cost([-1, -1, 4, 5, -1], 5) == -1
