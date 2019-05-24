from typing import Union, Optional


class Node:
    def __init__(self, data: Union[int, str]):
        self.data = data
        self.next: Optional[Node] = None


class Stack:
    def __init__(self, head: Node = None):
        self.head: Optional[Node] = head

    def push(self, data: Union[int, str]):
        node: Node = Node(data)

        if self.head:
            node.next = self.head

        self.head = node

        return self

    def pop(self) -> Node:
        if not self.head:
            raise Exception("Stack Underflow")

        head: Node = self.head
        self.head = self.head.next
        head.next = None
        return head

    def __len__(self) -> int:
        head = self.head
        count: int = 0

        while head:
            count += 1
            head = head.next

        return count

    def peek(self) -> Optional[Union[int, str]]:
        return self.head.data if self.head else None

    def is_empty(self) -> bool:
        return self.head is None
