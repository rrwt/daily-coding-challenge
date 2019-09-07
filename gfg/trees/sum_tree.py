"""
Given a Binary Tree where each node has positive and negative values.
Convert this to a tree where each node contains the sum of the left and
right sub trees in the original tree. The values of leaf nodes are changed to 0.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from tree_traversal import inorder  # type ignore


def sum_tree(root: Optional[Node]) -> int:
    if root is None:
        return 0

    return_value = root.data
    if root.left is None and root.right is None:
        root.data = 0
        return return_value

    left_sum = sum_tree(root.left)
    right_sum = sum_tree(root.right)
    root.data = left_sum + right_sum
    return return_value + root.data


if __name__ == "__main__":
    root = Node(50)
    root.left = Node(7)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(30)
    inorder(root)
    print()
    sum_tree(root)
    inorder(root)
    print()

    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)
    inorder(root)
    print()
    sum_tree(root)
    inorder(root)
    print()
