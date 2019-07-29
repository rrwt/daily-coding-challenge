"""
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""
from typing import Optional, Union
import operator

from binary_tree_node import Node  # type: ignore


sign_dict: dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def arithmetic_bin_tree(root: Optional[Node]) -> Union[int, float]:
    """
    Assuming everything is good. There are no corner cases
    Using Inorder tree traversal for calculation
    Time Complexity: O(n)
    Space Complexity: O(n) # stack
    """
    if not root:
        return 0

    left_num: Union[int, float] = arithmetic_bin_tree(root.left)

    if left_num:
        symbol = sign_dict[root.data]
        right_num: Union[int, float] = arithmetic_bin_tree(root.right)
        return symbol(left_num, right_num)

    return int(root.data)


if __name__ == "__main__":
    root = Node("*")
    root.left = Node("+")
    root.right = Node("+")
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.left = Node(4)
    root.right.right = Node(5)
    assert arithmetic_bin_tree(root) == 45
