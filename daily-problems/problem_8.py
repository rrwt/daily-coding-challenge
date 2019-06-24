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

from binary_tree_node import Node  # type: ignore


def count_unival(root: Optional[Node]) -> Tuple[int, bool]:
    """
    time complexity: O(n)
    space complexity: O(n)  # stack
    """
    if root is None:
        return 0, True

    left_unival, is_left = count_unival(root.left)
    right_unival, is_right = count_unival(root.right)

    count = left_unival + right_unival

    if is_left and is_right:
        if root.left and root.data != root.left.data:
            return count, False
        if root.right and root.data != root.right.data:
            return count, False

        return count + 1, True

    return count, False


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)
    print(count_unival(root)[0])
