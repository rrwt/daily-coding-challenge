"""
Given the root to a binary search tree, find the second largest node in the tree.
"""
from typing import Optional, Union

from binary_tree_node import Node  # type: ignore


def get_second_largest(root: Optional[Node]) -> Optional[Union[int, str]]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    If root has a right child, then largest/second largest node cannot be part of the left subtree
    If root doesn't have a right child, then the second largest node will be the largest element of
    left subtree
    """
    if not root:
        return None

    while root.right and (root.right.left or root.right.right):
        root = root.right

    if root.right:
        return root.data

    root = root.left

    while root and root.right:
        root = root.right

    return root.data if root else None


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    assert get_second_largest(root) == 7
