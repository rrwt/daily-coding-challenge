"""
You are given a set of n types of rectangular 3-D boxes,
where the ith box has height h(i), width w(i) and depth d(i).
You want to create a stack of boxes which is as tall as possible,
but you can only stack a box on top of another box
if the dimensions of the 2-D base of the lower box
are each strictly larger than those of the 2-D base of the higher box.
Of course, you can rotate a box so that any side functions as its base.
It is also allowable to use multiple instances of the same type of box.
"""
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Box:
    """
    A data class defining a 3D box
    """
    length: int
    width: int
    height: int


def get_rotations(boxes: List[Tuple[int]]) -> List[Box]:
    """
    Get all rotations of all boxes. Make length > width for easier comparisons
    This is useful for 2 reasons:
        1. We can use multiple copies of a box. e.g 4 * 2 * 5 can go on top of 5 * 4 * 2 (same box)
        2. We need to find the optimal base (as large as possible) for boxes on top
    """
    rotations = []

    for (l, b, h) in boxes:
        # 3 configurations per box.
        rotations.append(Box(max(l, b), min(l, b), h))
        rotations.append(Box(max(b, h), min(b, h), l))
        rotations.append(Box(max(h, l), min(h, l), b))

    return rotations


def has_smaller_base(box_1: Box, box_2: Box) -> bool:
    # Making use of the fact that length > width. No need for multiple comparisons
    return box_1.length < box_2.length and box_1.width < box_2.width


def stack_boxes(boxes: List[Tuple[int, ...]]) -> int:
    """
    Dynamic Programming.
    First, get all possible combinations of base (l*b) and height (h).
    Then, sort the given rotations based on maximum base area.
    Then, maximize the height given constraints.

    Time Complexity: O(n * n)
    Space Complexity: O(n)
    """
    all_rotations = sorted(
        get_rotations(boxes),
        key=lambda box: box.length * box.width,
        reverse=True
    )
    len_boxes = len(all_rotations)
    results = [0] * len_boxes

    for i in range(len_boxes):
        results[i] = all_rotations[i].height

        for j in range(i):
            if has_smaller_base(all_rotations[i], all_rotations[j]):
                results[i] = max(results[i], results[j] + all_rotations[i].height)

    return max(results)


if __name__ == "__main__":
    assert stack_boxes([(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)]) == 60
