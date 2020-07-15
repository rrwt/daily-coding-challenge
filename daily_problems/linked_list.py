from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None
