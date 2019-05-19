"""
design a stack which, in addition to push and pop, has a function min which
returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""
from random import randint

from stack import Node, Stack  # type: ignore


class MinOperationStack(Stack):
    def __init__(self, head: Node = None):
        super().__init__(head)
        self.min_stack = Stack()

    def push(self, data: int):
        super().push(data)

        if self.min_stack.head:
            head: Node = self.min_stack.head
            node: Node = Node(head.data) if head.data <= data else Node(data)
            node.next = self.min_stack.head
            self.min_stack.head = node
        else:
            self.min_stack.head = Node(data)

    def pop(self) -> Node:
        self.min_stack.head = self.min_stack.head.next
        return super().pop()

    def min(self):
        if self.min_stack.head:
            return self.min_stack.head.data


if __name__ == "__main__":
    stack = MinOperationStack()

    for i in range(10):
        stack.push(randint(0, 1000))

    head: Node = stack.head

    while head.next:
        print(head.data, end="->")
        head = head.next

    print(head.data)

    h_min = stack.min_stack.head

    while h_min.next:
        print(h_min.data, end="->")
        h_min = h_min.next

    print(h_min.data)
