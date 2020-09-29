from collections import deque
from typing import Union, Optional


class Node:
    """
    A Binary tree node with data element and upto 2 child nodes (left and right)
    """

    __slots__ = "data", "left", "right"

    def __init__(self, data: Union[int, str]):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def inorder_traversal(root: Optional[Node]) -> None:
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)


def level_order_traversal(root: Node) -> None:
    queue = deque()
    queue.append((root, 0))
    prev_level = 0

    while queue:
        node, level = queue.popleft()

        if level != prev_level:
            prev_level = level
            print()

        print(node.data, end=" ")

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    print()
