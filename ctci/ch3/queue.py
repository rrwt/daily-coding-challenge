from typing import Optional

from stack import Node  # type: ignore


class Queue:
    def __init__(self, head: Node = None):
        self.head = head

    def push(self, data: int):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            head = self.head

            while head.next:
                head = head.next
            head.next = node

    def pop(self) -> Optional[Node]:
        if not self.head:
            print("empty queue")
            return None
        else:
            node = self.head
            self.head = self.head.next

            return node
