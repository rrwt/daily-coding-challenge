"""
Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.

For example, given the following rectangles:
    { "top_left": (1, 4), "dimensions": (3, 3) # width, height }
and
    { "top_left": (0, 5), "dimensions": (4, 3) # width, height }

    return 6.
"""
from dataclasses import dataclass


@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int


def intersection_area(rectangle_1: Rectangle, rectangle_2: Rectangle) -> int:
    x_len = min(
        rectangle_1.x + rectangle_1.width, rectangle_2.x + rectangle_2.width
    ) - max(rectangle_1.x, rectangle_2.x)

    y_len = min(rectangle_1.y, rectangle_2.y) - max(
        rectangle_1.y - rectangle_1.height, rectangle_2.y - rectangle_2.height
    )

    if x_len > 0 and y_len > 0:
        return x_len * y_len
    else:
        return 0


if __name__ == "__main__":
    assert intersection_area(Rectangle(1, 4, 3, 3), Rectangle(0, 5, 4, 3)) == 6
    assert intersection_area(Rectangle(0, 5, 5, 5), Rectangle(4, 4, 3, 3)) == 3
    assert intersection_area(Rectangle(0, 5, 5, 5), Rectangle(1, 4, 2, 2)) == 4
    assert intersection_area(Rectangle(1, 1, 1, 1), Rectangle(5, 5, 1, 1)) == 0
