"""
Given a sorted array, convert it into a height-balanced binary search tree.
"""
from typing import List, Optional

from daily_problems.binary_tree_node import Node


def sorted_array_to_height_balanced_bst(array: List[int]) -> Optional[Node]:
    size = len(array)

    if size == 0:
        return None
    if size == 1:
        return Node(array[0])

    mid = size // 2

    root = Node(array[mid])
    root.left = sorted_array_to_height_balanced_bst(array[:mid])
    root.right = sorted_array_to_height_balanced_bst(array[mid + 1:])
    return root
