"""
Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child must
be less than or equal to the root and the key in the right child
must be greater than or equal to the root.
"""
import sys
from typing import Optional

from daily_problems.binary_tree_node import Node


def _is_bst(min_val: int, max_val: int, node: Optional[Node] = None) -> bool:
    if not node:
        return True

    if min_val < node.data < max_val:
        return _is_bst(min_val, node.data, node.left) and _is_bst(
            node.data, max_val, node.right
        )

    return False


def is_bst(node: Optional[Node] = None) -> bool:
    return _is_bst(-sys.maxsize, sys.maxsize, node)


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    assert is_bst(root) is True

    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(4)
    assert is_bst(root) is False
