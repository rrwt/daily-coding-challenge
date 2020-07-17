"""
Given a BST, transform it into greater sum tree where
each node contains sum of all nodes greater than that node.
"""
from typing import Optional

from gfg.trees.binary_tree_node import Node  # type: ignore
from gfg.trees.tree_traversal import inorder  # type: ignore


def greater_sum(root_node: Optional[Node]) -> None:
    """
    Time Complexity: O(n)
    Using reverse inorder traversal
    """

    def construct(node: Optional[Node]) -> None:
        nonlocal node_sum

        if node is not None:
            construct(node.right)

            node_sum = node_sum + node.data
            node.data = node_sum - node.data

            construct(node.left)

    node_sum: int = 0
    construct(root_node)


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
