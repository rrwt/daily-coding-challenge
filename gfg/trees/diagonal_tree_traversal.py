"""Diagonal Traversal of Binary Tree
Consider lines of slope -1 passing between nodes. Given a Binary Tree,
print all diagonal elements in a binary tree belonging to same line.
e.g. Input
        8
    3        10
1       6  7    14
     4        13
Output : 
Diagonal Traversal of binary tree : 
 8 10 14
 3 6 7 13
 1 4
"""
from collections import deque

from binary_tree_node import Node  # type: ignore


def diagonal_traversal(root: Node):
    queue = deque()
    queue.append([root, 0])

    while queue:
        node, level = queue.popleft()

        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.appendleft([node.right, level])
        if queue and queue[0][1] > level:
            print(node.data)
        else:
            print(node.data, end=" ")


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.left = Node(7)
    root.right.right = Node(14)
    root.left.right.left = Node(4)
    root.right.right.left = Node(13)
    diagonal_traversal(root)
