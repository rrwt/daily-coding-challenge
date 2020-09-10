"""
Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last,
and the nodes in the last level are filled starting from the left.
"""
from typing import Optional

from daily_problems.binary_tree_node import Node


def get_left_height(root_node: Node) -> int:
    node = root_node
    count = 0

    while node:
        count += 1
        node = node.left

    return count


def get_right_height(root_node: Node) -> int:
    node = root_node
    count = 0

    while node:
        count += 1
        node = node.right

    return count


def count_nodes(
    root_node: Node,
    left_height: Optional[int] = None,
    right_height: Optional[int] = None,
) -> int:
    # memoization. to not calculate height of a path more than once
    if not root_node:
        return 0

    left_height = left_height or get_left_height(root_node)
    right_height = right_height or get_right_height(root_node)

    if left_height == right_height:
        return (2 ** left_height) - 1

    return (
        1
        + count_nodes(root_node.left, left_height - 1)
        + count_nodes(root_node.right, None, right_height - 1)
    )


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(1)
    root.right = Node(1)
    assert count_nodes(root) == 3

    root.left.left = Node(1)
    assert count_nodes(root) == 4

    root.left.right = Node(1)
    assert count_nodes(root) == 5

    root.right.left = Node(1)
    assert count_nodes(root) == 6
