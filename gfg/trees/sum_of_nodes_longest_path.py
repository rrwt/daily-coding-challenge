"""
Given a binary tree containing n nodes. The problem is to find
the sum of all nodes on the longest path from root to leaf node.
If two or more paths compete for the longest path, then the path
having maximum sum of nodes is being considered.
"""
from typing import Optional, Tuple

from binary_tree_node import Node  # type: ignore


def sum_of_nodes(root: Optional[Node]) -> Tuple[int, int]:
    if root is None:
        return 0, 0

    left_sum, left_level = sum_of_nodes(root.left)
    right_sum, right_level = sum_of_nodes(root.right)
    curr_sum, curr_level = 0, 0

    if left_level > right_level:
        curr_sum, curr_level = left_sum, left_level
    elif right_level > left_level:
        curr_sum, curr_level = right_sum, right_level
    else:
        curr_sum, curr_level = max(left_sum, right_sum), left_level

    return curr_sum + int(root.data), curr_level + 1


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(1)
    root.right.left = Node(2)
    root.right.right = Node(3)
    root.left.right.left = Node(6)

    assert sum_of_nodes(root)[0] == 13
