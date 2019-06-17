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
