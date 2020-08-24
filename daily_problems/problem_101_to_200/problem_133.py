"""
Given a node in a binary search tree,
return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35

You can assume each node has a parent pointer.
"""
from typing import Optional


class Node:

    def __init__(self, data: int, parent: Optional['Node'] = None) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


def inorder_successor(node: Node) -> int:
    if node.right:
        node = node.right

        while node.left:
            node = node.left

        return node.data
    elif node.parent and node.parent.data > node.data:
        return node.parent.data
    else:
        return -1


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5, root)
    root.right = Node(30, root)
    root.right.left = Node(22, root.right)
    root.right.right = Node(35, root.right)
    assert inorder_successor(root) == 22
    assert inorder_successor(root.left) == 10
    assert inorder_successor(root.right) == 35
    assert inorder_successor(root.right.left) == 30
    assert inorder_successor(root.right.right) == -1
