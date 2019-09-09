"""
The diameter of a tree (sometimes called the width) is the
number of nodes on the longest path between two end nodes.
"""
from typing import Optional
from collections import defaultdict

from binary_tree_node import Node  # type: ignore


def height(root: Optional[Node]) -> int:
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def diameter_inefficient(root: Optional[Node]) -> int:
    """
    Diameter = max of left diameter, right diameter, left height + right height + 1
    Time Complexity: O(n*n)
    Space Complexity: O(n)
    """
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left_height = height(root.left)
    right_height = height(root.right)
    left_diameter = diameter_inefficient(root.left)
    right_diameter = diameter_inefficient(root.right)

    return max(left_height + right_height + 1, left_diameter, right_diameter)


def diameter_efficient(root: Optional[Node]) -> int:
    """
    Calculate height while calculating the diameter
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def diameter(root: Optional[Node]):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            height[root.data] = 1
            return 1

        d_left = diameter(root.left)
        d_right = diameter(root.right)
        height[root.data] = max(height[root.left.data], height[root.right.data]) + 1

        return max(
            d_left, d_right, 1 + height[root.left.data] + height[root.right.data]
        )

    height = defaultdict(int)
    return diameter(root)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    assert diameter_inefficient(root) == 4
    assert diameter_efficient(root) == 4
