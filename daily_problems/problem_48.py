"""
Given pre-order and in-order traversals of a binary tree,
write a function to reconstruct the tree.
For example, given the following preorder traversal: [a, b, d, e, c, f, g]
And the following inorder traversal: [d, b, e, a, f, c, g]
You should return the following tree:
    a
  b   c
d  e f  g
"""
from typing import Optional

from binary_tree_node import Node, inorder_traversal  # type: ignore


def reconstruct_tree(preorder: list, inorder: list) -> Optional[Node]:
    """
    First element of preorder is the root.
    Find root in inorder, all the elements to the left of root in
    an inorder traversal are part of left subtree and to the right are
    part of the right subtree.
    """

    def tree(start: int, end: int) -> Optional[Node]:
        nonlocal inorder_dict, l, index

        if start > end or start >= l:
            return None

        element: str = preorder[index]
        root: Node = Node(element)
        index += 1  # preorder traversal
        in_index: int = inorder_dict[element]

        if start < end:  # inorder traversal
            root.left = tree(start, in_index - 1)
            root.right = tree(in_index + 1, end)

        return root

    inorder_dict: dict = {value: key for key, value in enumerate(inorder)}
    l = len(preorder)
    index: int = 0
    return tree(0, l - 1)


if __name__ == "__main__":
    preorder: list = ["a", "b", "d", "e", "c", "f", "g"]
    inorder: list = ["d", "b", "e", "a", "f", "c", "g"]
    inorder_traversal(reconstruct_tree(preorder, inorder))
