"""
Construct a complete binary tree from given array in level order fashion
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from depth_first_traversal_recursive import inorder  # type: ignore


def complete_binary_tree(level_order: list) -> Optional[Node]:
    """
    time complexity: O(n)
    space complexity: O(n)  # stack
    """

    def tree(index: int) -> Optional[Node]:
        if index >= l:
            return None

        node = Node(level_order[index])
        node.left = tree(2 * index + 1)
        node.right = tree(2 * index + 2)
        return node

    l: int = len(level_order)
    return tree(0)


if __name__ == "__main__":
    print(inorder(complete_binary_tree([1, 2, 3, 4, 5, 6])))
