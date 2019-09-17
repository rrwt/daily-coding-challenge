"""
bst from preorder traversal
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from tree_traversal import inorder  # type: ignore


def construct_bst(preorder: list) -> Optional[Node]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)  # stack

    Using static index variable alongwith min and max values
    """

    def construct(min_val: int, max_val: int) -> Optional[Node]:
        nonlocal index, length

        if index >= length or preorder[index] < min_val or preorder[index] > max_val:
            return None

        root = Node(preorder[index])
        index += 1
        root.left = construct(min_val, root.data)
        root.right = construct(root.data, max_val)
        return root

    index: int = 0
    length: int = len(preorder)
    return construct(-1_000_000, 1_000_000)


if __name__ == "__main__":
    preorder: list = [10, 5, 1, 7, 40, 50]
    root = construct_bst(preorder)
    inorder(root)
    print()
