"""
Construct Full Binary Tree using its Preorder traversal and Preorder traversal
of its mirror tree
Full Binary Tree: One whose every node has 0 or 2 children
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from depth_first_traversal_recursive import inorder  # type: ignore


def full_binary_tree(preorder: list, mirror: list) -> Optional[Node]:
    d = {k: v for v, k in enumerate(mirror)}

    def tree(start: int, end: int) -> Optional[Node]:
        nonlocal pre_index

        if start > end or pre_index >= l:
            return None

        node = Node(preorder[pre_index])
        pre_index += 1

        if start == end or pre_index >= l:
            return node

        mirror_index = d[preorder[pre_index]]

        if mirror_index <= end:
            node.left = tree(mirror_index, end)
            node.right = tree(start + 1, mirror_index - 1)

        return node

    l = len(preorder)
    pre_index = 0
    return tree(0, l - 1)


if __name__ == "__main__":
    print(inorder(full_binary_tree([1, 2, 4, 5, 3, 6, 7], [1, 3, 7, 6, 2, 5, 4])))
