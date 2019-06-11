"""
Given a BST, transform it into greater sum tree where each node contains sum of
all nodes greater than that node.
"""
from typing import Optional

from bst_and_node import Node, inorder  # type: ignore


def greater_sum_bst(root: Node) -> Node:
    """
    time complexity: O(n)
    space complexity: O(n)
    """
    def construct(node: Optional[Node]) -> Optional[Node]:
        """
        Reverse inorder traversal
        """
        nonlocal total

        if node:
            construct(node.right)
            node.data, total = total, total + node.data
            construct(node.left)

        return node

    total: int = 0
    return construct(root)


if __name__ == "__main__":
    root = Node(11)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right = Node(29)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.left = Node(35)

    inorder(greater_sum_bst(root))
