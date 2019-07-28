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
