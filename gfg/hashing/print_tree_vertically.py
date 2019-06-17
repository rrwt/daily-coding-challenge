"""
Given a binary tree, print it vertically. e.g.
         1
        /    \ 
       2      3
      / \   /   \
     4   5  6   7
               /  \ 
              8   9 
             
The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9
"""
from typing import Optional
from collections import defaultdict

from binary_tree_node import Node  # type: ignore


def print_vertically(root: Node):
    """
    time complexity: O(n)
    space complexity: O(n)
    """

    def inorder(node: Optional[Node], distance: int):
        nonlocal dist, min_, max_

        if not node:
            return

        if distance < min_:
            min_ = distance
        elif distance > max_:
            max_ = distance

        dist[distance].append(node.data)
        inorder(node.left, distance - 1)
        inorder(node.right, distance + 1)

    dist: defaultdict = defaultdict(list)
    min_, max_ = 0, 0
    inorder(root, 0)

    for i in range(min_, max_ + 1):
        print(*dist[i])


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.left = Node(8)
    root.right.right.right = Node(9)

    print_vertically(root)
