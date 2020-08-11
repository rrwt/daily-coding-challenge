"""
Given a Binary Tree, find size of the Largest Independent Set(LIS) in it.
A subset of all tree nodes is an independent set if there is no edge between
any two nodes of the subset.

For example, consider the following binary tree.
        10
    20        30
40      50         60
     70    60
The largest independent set(LIS) is {10, 40, 60, 70, 80} and size of the LIS is 5.
"""
from typing import Optional


class TabulatedNode:

    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.max_inc: Optional[int] = None
        self.max_exc: Optional[int] = None


def lis_size_recursive(
        node: Optional[TabulatedNode] = None,
        parent_selected: Optional[bool] = False
) -> int:
    """
    Time Complexity: (2^n) because there are 2 choices at every step.
    Space Complexity: O(h)  # height of the tree
    """
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 0 if parent_selected else 1

    max_count = 0

    if not parent_selected:
        max_count = 1 + lis_size_recursive(node.left, True) + lis_size_recursive(node.right, True)

    return max(
        max_count, lis_size_recursive(node.left, False) + lis_size_recursive(node.right, False)
    )


def lis_size_dp(
        node: Optional[TabulatedNode] = None,
        parent_selected: Optional[bool] = None
) -> int:
    """
    We add extra params to node for tabulation
    """
    if node is None:
        return 0

    if node.left is None and node.right is None:
        if node.max_inc is None:
            node.max_inc = 1
            node.max_exc = 0

        return node.max_exc if parent_selected else node.max_inc

    if not parent_selected:
        if node.max_inc is None:
            node.max_inc = 1 + lis_size_dp(node.left, True) + lis_size_dp(node.right, True)

    if node.max_exc is None:
        node.max_exc = lis_size_dp(node.left, False) + lis_size_dp(node.right, False)

    return max(node.max_inc or 0, node.max_exc or 0)


if __name__ == "__main__":
    root = TabulatedNode(10)
    root.left = TabulatedNode(20)
    root.right = TabulatedNode(30)
    root.left.left = TabulatedNode(40)
    root.right.right = TabulatedNode(60)
    root.left.right = TabulatedNode(50)
    root.left.right.left = TabulatedNode(70)
    root.left.right.right = TabulatedNode(60)

    assert lis_size_recursive(root) == 5
    assert lis_size_dp(root) == 5
