"""
Construct a tree from given inorder and preorder traversals
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from depth_first_traversal_recursive import inorder  # type: ignore


def construct_tree(inorder: list, preorder: list) -> Optional[Node]:
    """
    time complexity: O(n)
    space complexity: O(n)
    """

    d = {k: v for v, k in enumerate(inorder)}

    def tree(start: int, end: int) -> Optional[Node]:
        nonlocal pre_index

        if pre_index >= l or start > end:
            return None

        value = preorder[pre_index]
        node = Node(value)
        in_index = d.get(value) or -1
        pre_index += 1

        if start < end:
            node.left = tree(start, in_index - 1)
            node.right = tree(in_index + 1, end)

        return node

    l: int = len(inorder)
    pre_index = 0
    return tree(0, l - 1)


if __name__ == "__main__":
    inorder(
        construct_tree(["D", "B", "E", "A", "F", "C"], ["A", "B", "D", "E", "C", "F"])
    )
