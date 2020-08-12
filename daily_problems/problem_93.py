"""
Given a tree, find the largest tree/subtree that is a BST.
Given a tree, return the size of the largest tree/subtree that is a BST.
"""
import sys
from typing import Optional, Tuple

from daily_problems.binary_tree_node import Node


def _largest_bst(
    min_val: int, max_val: int, root_node: Optional[Node] = None
) -> Tuple[Optional[Node], bool, int]:
    """
    min_val and max_val are helper variables, helping us make sure that if the values of a node
    lie between them, then the node is part of a bst iff left and right child are bst
    Time Complexity: O(n)
    Space Complexity: (n)
    """
    if root_node is None:
        return None, False, 0

    if root_node.left is None and root_node.right is None:
        return root_node, True, 1

    left_bst, is_left_bst, size_left = _largest_bst(
        min_val, root_node.data, root_node.left
    )
    right_bst, is_right_bst, size_right = _largest_bst(
        root_node.data, max_val, root_node.right
    )

    if (
        is_left_bst
        and is_right_bst
        and root_node.left.data < root_node.data < root_node.right.data
    ):
        return root_node, True, size_left + size_right + 1

    if size_left >= size_right:
        return left_bst, False, size_left

    return right_bst, False, size_right


def largest_bst(root_node: Optional[Node] = None) -> Tuple[Optional[Node], int]:
    bst_node, is_bst, size = _largest_bst(-sys.maxsize, sys.maxsize, root_node)
    return bst_node, size


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(1)
    root.left.right = Node(3)

    response = largest_bst(root)
    assert response[0].data == 2
    assert response[1] == 3

    root = Node(50)
    root.left = Node(30)
    root.right = Node(60)
    root.left.left = Node(5)
    root.left.right = Node(20)
    root.right.left = Node(45)
    root.right.right = Node(70)
    root.right.right.left = Node(65)
    root.right.right.right = Node(80)

    response = largest_bst(root)
    assert response[0].data == 60
    assert response[1] == 5
