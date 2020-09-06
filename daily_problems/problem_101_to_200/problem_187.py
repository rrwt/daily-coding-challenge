"""
You are given given a list of rectangles represented by min and max x- and y-coordinates.
Compute whether or not a pair of rectangles overlap each other.
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return true as the first and third rectangle overlap each other.
"""
from typing import List
from itertools import combinations

from daily_problems.problem_101_to_200.problem_185 import intersection_area
from daily_problems.problem_101_to_200.problem_185 import Rectangle


def overlapping_rectangles(rectangles: List[Rectangle]) -> bool:
    for r1, r2 in combinations(rectangles, 2):
        if bool(intersection_area(r1, r2)):
            return True

    return False


if __name__ == "__main__":
    assert (
        overlapping_rectangles(
            [Rectangle(1, 4, 3, 3), Rectangle(-1, 3, 2, 1), Rectangle(0, 5, 4, 3)]
        )
        is True
    )
