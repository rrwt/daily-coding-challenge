"""
Given a binary tree, determine whether or not it is height-balanced.
A height-balanced binary tree can be defined as one in which the
heights of the two subtrees of any node never differ by more than one.
"""
from typing import Tuple

from daily_problems.binary_tree_node import Node


def height_balanced(node: Node) -> Tuple[bool, int]:
    if node is None:
        return True, 0
    if node.left is None and node.right is None:
        return True, 1

    is_balanced_left, height_left = height_balanced(node.left)

    if not is_balanced_left:
        return is_balanced_left, height_left

    is_balanced_right, height_right = height_balanced(node.right)

    if not is_balanced_right or abs(height_right - height_left) > 1:
        return False, max(height_right, height_left)

    return True, max(height_right, height_left) + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(7)
    root.right.left = Node(6)
    assert height_balanced(root)[0] is True
