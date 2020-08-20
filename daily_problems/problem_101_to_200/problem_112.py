"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia:
    The lowest common ancestor is defined between two nodes v and w
    as the lowest node in T that has both v and w as descendants
    (where we allow a node to be a descendant of itself).”
"""
from typing import Optional

from daily_problems.binary_tree_node import Node


def lca(first: int, second: int, root_node: Optional[Node] = None) -> Optional[int]:
    """
    Assuming all nodes have unique value.
    Assuming either both first and second are present or both are absent
    Time complexity: O(n)
    Space Complexity: O(n)
    """
    if root_node is None:
        return None

    if root_node.data in (first, second):
        return root_node.data

    left_anc = lca(first, second, root_node.left)
    right_anc = lca(first, second, root_node.right)

    if left_anc and right_anc:
        return root_node.data
    if left_anc:
        return left_anc
    return right_anc


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    assert lca(4, 5, root) == 2
    assert lca(4, 6, root) == 1
    assert lca(3, 4, root) == 1
    assert lca(2, 4, root) == 2
