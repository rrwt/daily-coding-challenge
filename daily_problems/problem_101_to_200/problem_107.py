"""
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.
  1
 / \
2   3
   / \
  4   5
"""
from collections import deque
from typing import Optional

from daily_problems.binary_tree_node import Node


def bfs_tree(root_node: Optional[Node]) -> None:
    """
    O(n) and O(n)
    """
    if not root_node:
        return None

    q = deque()
    q.append(root_node)

    while q:
        cur_node = q.popleft()
        print(cur_node.data)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.right.left = Node(4)
    tree.right.right = Node(5)
    bfs_tree(tree)
