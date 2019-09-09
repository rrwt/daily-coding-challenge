"""
Merge Two Binary Trees by doing Node Sum (Recursive and Iterative)
Given two binary trees. We need to merge them into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up
as the new value of the merged node. Otherwise, the non-null node will
be used as the node of new tree.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from tree_traversal import inorder  # type: ignore


def merge_sum_tree(augend: Optional[Node], addend: Optional[Node]) -> Optional[Node]:
    if augend is None and addend is None:
        return None

    if augend is None:
        return addend
    if addend is None:
        return augend

    root = Node(augend.data + addend.data)
    root.left = merge_sum_tree(augend.left, addend.left)
    root.right = merge_sum_tree(augend.right, addend.right)

    return root


if __name__ == "__main__":
    augend = Node(2)
    augend.left = Node(1)
    augend.right = Node(4)
    augend.left.left = Node(5)

    addend = Node(3)
    addend.left = Node(6)
    addend.right = Node(1)
    addend.left.right = Node(2)
    addend.right.right = Node(7)

    root = merge_sum_tree(augend, addend)
    inorder(root)
