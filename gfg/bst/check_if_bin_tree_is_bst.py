"""
A program to check if a binary tree is BST or not
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.
"""
from typing import Optional

from gfg.bst.bst_and_node import Node  # type: ignore


def is_bst(root: Node) -> bool:
    """
    time complexity: O(n)
    Space complexity: O(n)
    :param root: Node
    :return: bool
    """
    def check_bst(node: Optional[Node], min_: int, max_: int) -> bool:
        if not node:
            return True

        if node.data < min_ or node.data > max_:
            return False

        return check_bst(node.left, min_, max_ - 1) and check_bst(node.right, min_ + 1, max_)

    return check_bst(root, -1000_000, 1000_000)


def is_bst_using_in_order_traversal(root: Node) -> bool:
    """
    time complexity: O(n)
    Space complexity: O(n)
    :param root: Node
    :return: bool
    """
    def in_order(node: Optional[Node]):
        nonlocal elems
        if node:
            in_order(node.left)
            elems.append(node.data)  # should be sorted
            in_order(node.right)

    elems: list = []
    in_order(root)

    for i in range(1, len(elems)):
        if elems[i-1] > elems[i]:
            return False

    return True


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(is_bst(root))
    print(is_bst_using_in_order_traversal(root))
