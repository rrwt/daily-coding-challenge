"""
Construct Full Binary Tree from given preorder and postorder traversals
Full Binary Tree: One whose every node has 0 or 2 children
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from depth_first_traversal_recursive import inorder  # type: ignore


def full_binary_tree(preorder: list, postorder: list) -> Optional[Node]:
    d = {k: v for v, k in enumerate(postorder)}

    def tree(start: int, end: int) -> Optional[Node]:
        nonlocal pre_index

        if pre_index >= l or start > end:
            return None

        value = preorder[pre_index]
        node = Node(value)
        pre_index += 1

        if start == end or pre_index >= l:
            return node

        post_index: int = d[preorder[pre_index]]

        if post_index <= end:
            node.left = tree(start, post_index)
            node.right = tree(post_index + 1, end)

        return node

    l = len(preorder)
    pre_index = 0
    return tree(0, l - 1)


if __name__ == "__main__":
    print(
        inorder(
            full_binary_tree([1, 2, 4, 8, 9, 5, 3, 6, 7], [8, 9, 4, 5, 2, 6, 7, 3, 1])
        )
    )
