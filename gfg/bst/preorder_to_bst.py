"""
Given preorder traversal of a binary search tree, construct the BST.
"""
from typing import Optional
from array import array

from gfg.bst.bst_and_node import Node, inorder


def construct_bst(
        preorder: array, start: Optional[int] = None, end: Optional[int] = None
) -> Optional[Node]:
    """
    BST: left - smaller than current
         right - bigger than current
    """
    if start is None:
        start = 0
    if end is None:
        end = len(preorder) - 1
    if start > end:
        return None

    node = Node(preorder[start])

    if start < end:
        index = start + 1

        while index < end and preorder[index] < preorder[start]:
            index += 1

        node.left = construct_bst(preorder, start+1, index-1)
        node.right = construct_bst(preorder, index, end)

    return node


if __name__ == "__main__":
    inorder(construct_bst(array("I", [10, 5, 1, 7, 40, 50])))
