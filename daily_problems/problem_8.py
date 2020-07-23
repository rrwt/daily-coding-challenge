"""
A unival tree (which stands for "universal value") is a tree
where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
from typing import Tuple, Optional

from daily_problems.binary_tree_node import Node  # type: ignore


def count_unival(root_node: Optional[Node] = None) -> Tuple[int, bool]:
    """
    time complexity: O(n)
    space complexity: O(n)  # stack
    """
    if root_node is None:
        return 0, True

    count_left, is_left_unival = count_unival(root_node.left)
    count_right, is_right_unival = count_unival(root_node.right)
    total_count = count_left + count_right

    if is_left_unival and is_right_unival:
        if (root_node.left and root_node.data != root_node.left.data) or (
                root_node.right and root_node.data != root_node.right.data
        ):
            return total_count, False
        return total_count + 1, True

    return total_count, False


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)
    print(count_unival(root)[0])
