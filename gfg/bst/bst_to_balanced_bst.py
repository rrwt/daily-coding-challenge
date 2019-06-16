"""
Given a bst, convert it to a balanced bst
"""
from typing import Optional

from bst_and_node import Node, inorder  # type: ignore
from check_if_bst_is_balanced import is_balanced  # type: ignore
from check_if_bin_tree_is_bst import is_bst  # type: ignore
from sorted_arr_to_bst import sorted_arr_to_bst  # type: ignore


def bst_to_balanced_bst(root: Node) -> Node:
    """
    Steps:
        1. Get sorted array from bst i.e. inorder traversal: O(n) & O(n)
        2. create a balanced bst from sorted array: O(n) & O(n)
    Overall complexity:
        time: O(n)
        space: O(n)
    """

    def get_inorder_array(node: Optional[Node]):
        nonlocal arr

        if node:
            get_inorder_array(node.left)
            arr.append(node.data)
            get_inorder_array(node.right)

    arr: list = []

    return sorted_arr_to_bst(arr)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(5)
    tree = bst_to_balanced_bst(root)
    print(is_bst(tree))
    print(is_balanced(tree))
