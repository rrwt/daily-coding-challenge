"""
Given a binary tree of integers, find the maximum path sum between two nodes.
The path must go through at least one node, and does not need to go through the root.
"""
from typing import Optional, Tuple

from daily_problems.binary_tree_node import Node


def _max_sum_path(root_node: Optional[Node]) -> Tuple[int, int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(h)  # height
    :returns: Tuple[max sum with root_node as root, max sum with root_node + one of child tree]
    """
    if root_node is None:
        return 0, 0

    left_sum_tree, left_sum_node = 0, 0
    right_sum_tree, right_sum_node = 0, 0

    if root_node.left:
        left_sum_tree, left_sum_node = _max_sum_path(root_node.left)
    if root_node.right:
        right_sum_tree, right_sum_node = _max_sum_path(root_node.right)

    return (
        left_sum_node + right_sum_node + root_node.data,
        root_node.data + max(left_sum_tree, right_sum_tree),
    )


def max_sum_path(root_node: Optional[Node] = None) -> int:
    return max(*_max_sum_path(root_node))


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    assert max_sum_path(root) == 42
