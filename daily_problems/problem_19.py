"""
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are
of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build
the nth house with kth color, return the minimum cost which achieves this goal.
"""
import sys
from typing import List


def color_houses_backtrack(house_colors: List[List[int]], n: int, k: int) -> int:
    """
    Using backtracking solution. 2^n
    """

    def util_backtrack(house: int) -> int:
        nonlocal n, k, color_dict, house_colors

        if house >= n:
            return 0

        min_cost = sys.maxsize

        for color in range(k):
            cost = house_colors[house][color]

            if house == 0 or color_dict[house - 1] != color:
                color_dict[house] = color
                cost += util_backtrack(house + 1)

                if cost < min_cost:
                    min_cost = cost

        return min_cost

    color_dict = [None] * n
    return util_backtrack(0)


def color_houses_dp(house_colors: List[List[int]], n: int, k: int) -> int:
    """
    For k colors, find the least cost so far if current house is painted with ith color.
    It in current iteration, the house is painted with ith color, then in previous it must've been
    painted with any other color. Calculate this price recursively while ensuring that it is minimum
    Time Complexity: O(k*n)
    Space Complexity: O(k)
    """
    # we update these values for each new house while ensuring that we have the best configuration
    # so far.
    colors: List[int] = [house_colors[0][i] for i in range(k)]

    for house in range(1, n):
        min1, min2 = colors[0], colors[1]
        index1, index2 = 0, 1

        if min1 > min2:
            min1, min2 = min2, min1
            index1, index2 = index2, index1

        for i in range(2, k):
            if colors[i] <= min1:
                min1, min2 = colors[i], min1
                index1, index2 = i, index1
            elif colors[i] < min2:
                min2 = colors[i]
                index2 = i

        for color in range(k):
            if color != index1:
                colors[color] = min1 + house_colors[house][color]
            else:
                colors[color] = min2 + house_colors[house][color]

    return min(colors)


if __name__ == "__main__":
    house_colors = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
    print(color_houses_backtrack(house_colors, 4, 3))
    print(color_houses_dp(house_colors, 4, 3))
