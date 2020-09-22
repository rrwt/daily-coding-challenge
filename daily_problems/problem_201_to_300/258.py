"""
In Ancient Greece, it was common to write text with the first line going left to right,
the second line going right to left, and continuing to go back and forth.
This style was called "boustrophedon".
Given a binary tree, write an algorithm to print the nodes in boustrophedon order.
For example, given the following tree:
       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].
"""
from typing import List

from daily_problems.binary_tree_node import Node


def boustrophedon(root_node: Node) -> List[int]:
    stack_1 = [root_node]
    stack_2 = []
    res = []

    while stack_1 or stack_2:
        if stack_1:
            while stack_1:
                node = stack_1.pop()
                res.append(node.data)

                if node.left:
                    stack_2.append(node.left)
                if node.right:
                    stack_2.append(node.right)
        elif stack_2:
            while stack_2:
                node = stack_2.pop()
                res.append(node.data)

                if node.right:
                    stack_1.append(node.right)
                if node.left:
                    stack_1.append(node.left)

    return res


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    assert boustrophedon(root) == [1, 3, 2, 4, 5, 6, 7]
