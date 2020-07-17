"""
given a bst, check if it is balanced
"""
from typing import Optional
from functools import lru_cache

from gfg.bst.bst_and_node import Node  # type: ignore


@lru_cache(128)
def height(root: Optional[Node]) -> int:
    """
    LRU cache will help us with recursive calls
    """
    if not root:
        return 0

    return max(height(root.left), height(root.right)) + 1


def is_balanced(root: Optional[Node]) -> bool:
    """
    time complexity: O(n)
    space complexity: O(n)  # stack
    """
    if not root:
        return True

    h_l = height(root.left)
    h_r = height(root.right)

    return abs(h_l - h_r) <= 1 and is_balanced(root.left) and is_balanced(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.left.left = Node(7)
    assert is_balanced(root)
