"""
Given a binary tree containing n nodes. The problem is to find the sum
of all the parent node’s which have a child node with value x.
"""
from typing import Optional, Tuple

from binary_tree_node import Node  # type: ignore


def sum_parent(root: Optional[Node], node: int) -> Tuple[int, bool]:
    if root is None:
        return 0, False

    left_sum, has_left_node = sum_parent(root.left, node)
    right_sum, has_right_node = sum_parent(root.right, node)
    result_sum = 0

    if has_left_node:
        result_sum += left_sum
    if has_right_node:
        result_sum += right_sum

    result_sum += int(root.data) if has_right_node or has_left_node else 0
    return result_sum, has_left_node or has_right_node or root.data == node


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(2)
    root.right.left = Node(2)
    root.right.right = Node(3)
    assert sum_parent(root, 2)[0] == 11
