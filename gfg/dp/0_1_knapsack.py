"""0/1 Knapsack
Given weights and values of n items, put these items in a knapsack
of capacity W to get the maximum total value in the knapsack. In other
words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent
values and weights associated with n items respectively. Also given an
integer W which represents knapsack capacity, find out the maximum value
subset of val[] such that sum of the weights of this subset is smaller
than or equal to W. You cannot break an item, either pick the complete
item, or don’t pick it (0-1 property).
"""
from typing import List


def zero_one_knapsack_naive(w: int, weights: list, values: list, index: int) -> int:
    """
    Either keep or leave the item
    """
    if w == 0 or index < 0:
        return 0

    max_value = 0

    if w >= weights[index]:
        max_value = values[index] + zero_one_knapsack_naive(
            w - weights[index], weights, values, index - 1
        )  # take

    return max(max_value, zero_one_knapsack_naive(w, weights, values, index - 1))  # leave


def zero_one_knapsack_tabulated(w: int, weights: list, values: list) -> int:
    length: int = len(weights)
    matrix: List[List[int]] = [[0] * (w + 1) for _ in range(length + 1)]

    for index in range(1, length + 1):
        for cur_weight in range(1, w + 1):
            if cur_weight >= weights[index - 1]:
                matrix[index][cur_weight] = max(
                    values[index - 1] + matrix[index - 1][cur_weight - weights[index - 1]],
                    matrix[index - 1][cur_weight],
                )
            else:
                matrix[index][cur_weight] = matrix[index - 1][cur_weight]

    return matrix[length][w]


if __name__ == "__main__":
    assert zero_one_knapsack_naive(50, [10, 20, 30], [60, 100, 120], 2) == 220
    assert zero_one_knapsack_tabulated(50, [10, 20, 30], [60, 100, 120]) == 220
