"""
Given the root of a binary tree, find the most frequent subtree sum.
The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:
  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
"""
from collections import defaultdict
from typing import Tuple

from daily_problems.binary_tree_node import Node


def _subtree_sum(root_node: Node, count: dict) -> Tuple[dict, int]:
    if not root_node:
        return count, 0
    if root_node.left is None and root_node.right is None:
        count[root_node.data] += 1
        return count, root_node.data

    count, left_sum = _subtree_sum(root_node.left, count)
    count, right_sum = _subtree_sum(root_node.right, count)
    total = left_sum + right_sum + root_node.data
    count[total] += 1
    return count, total


def subtree_sum(root_node: Node) -> int:
    count, _ = _subtree_sum(root_node, defaultdict(int))

    max_occ = 0
    return_val = 0

    for key, value in count.items():
        if value > max_occ:
            return_val = key
            max_occ = value

    return return_val


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(-5)
    assert subtree_sum(root) == 2
