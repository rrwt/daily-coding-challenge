"""
A program to check if a binary tree is BST or not
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.
"""
from typing import Optional

from bst_and_node import Node  # type: ignore


def is_bst(root: Node) -> bool:
    def check_bst(node: Optional[Node], min_: int, max_: int) -> bool:
        if not node:
            return True

        if node.data < min_ or node.data > max_:
            return False

        return check_bst(node.left, min_, max_ - 1) and check_bst(node.right, min_ + 1, max_)

    return check_bst(root, -1000_000, 1000_000)


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(is_bst(root))
