"""
Given two non-empty binary trees s and t, check whether tree t
has exactly the same structure and node values with a subtree of s.

A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
"""
from typing import Optional

from daily_problems.binary_tree_node import Node


def is_subtree_naive(root_1: Optional[Node] = None, root_2: Optional[Node] = None) -> bool:
    """
    Time Complexity: O(m*n)
    """
    if root_2 is None:
        return True
    if root_1 is None:
        return False

    is_sub = False

    if root_1.data == root_2.data:
        is_sub = is_subtree_naive(root_1.left, root_2.left) and is_subtree_naive(
            root_1.right, root_2.right
        )

    return is_sub or is_subtree_naive(root_1.left, root_2) or is_subtree_naive(root_1.right, root_2)


def is_subtree_fast(root_node_1: Optional[Node] = None, root_node_2: Optional[Node] = None) -> bool:
    """
    Tree S is a subtree of T if both inorder and preorder traversals of S
    are substrings of inorder and preorder traversals of T respectively.

    Time Complexity: O(n+m), given that substring search is O(n+m) using KMP or Rabin-Karp
    """
    def inorder(root: Optional[Node] = None) -> str:
        if not root:
            return ""
        return inorder(root.left) + str(root.data) + inorder(root.right)

    def preorder(root: Optional[Node] = None) -> str:
        if not root:
            return ""

        return str(root.data) + preorder(root.left) + preorder(root.right)

    first_inorder = inorder(root_node_1)
    first_preorder = preorder(root_node_1)
    second_inorder = inorder(root_node_2)
    second_preorder = preorder(root_node_2)

    return first_inorder.find(second_inorder) > -1 and first_preorder.find(second_preorder) > -1


if __name__ == "__main__":
    first = Node(26)
    first.right = Node(3)
    first.right.right = Node(3)
    first.left = Node(10)
    first.left.left = Node(4)
    first.left.left.right = Node(30)
    first.left.right = Node(6)

    second = Node(10)
    second.right = Node(6)
    second.left = Node(4)
    second.left.right = Node(30)
    assert is_subtree_naive(first, second) is True
    assert is_subtree_fast(first, second) is True

    third = Node(10)
    third.left = Node(6)
    third.right = Node(4)
    third.left.right = Node(30)
    assert is_subtree_naive(first, third) is False
    assert is_subtree_fast(first, third) is False
