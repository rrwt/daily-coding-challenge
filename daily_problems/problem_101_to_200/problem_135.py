"""
Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \    \
  2    1
      / \
    -1   2
"""
from typing import Optional

from daily_problems.binary_tree_node import Node


def min_sum_path_root_to_leaf(root: Optional[Node]) -> int:
    if not root:
        return 0
    if root.left is None and root.right is None:
        return root.data
    return root.data + min(
        min_sum_path_root_to_leaf(root.left), min_sum_path_root_to_leaf(root.right)
    )


if __name__ == "__main__":
    tree = Node(10)
    tree.left = Node(5)
    tree.right = Node(5)
    tree.left.right = Node(2)
    tree.right.right = Node(1)
    tree.right.right.left = Node(-1)
    tree.right.right.right = Node(2)

    assert min_sum_path_root_to_leaf(tree) == 15
