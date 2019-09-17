"""
Given a BST, transform it into greater sum tree where
each node contains sum of all nodes greater than that node.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from tree_traversal import inorder  # type: ignore


def greater_sum(root: Optional[Node]) -> None:
    """
    Time Complexity: O(n)
    Using reverse inorder traversal
    """

    def construct(root: Optional[Node]) -> None:
        nonlocal node_sum

        if root is not None:
            construct(root.right)

            node_sum = node_sum + root.data
            root.data = node_sum - root.data

            construct(root.left)

    node_sum: int = 0
    construct(root)


if __name__ == "__main__":
    root = Node(11)
    root.left = Node(2)
    root.right = Node(29)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.left = Node(35)

    greater_sum(root)
    inorder(root)
    print()
