"""
Implement a MyQueue class which implements a queue using two stacks.
"""
from typing import Optional

from stack import Stack, Node  # type: ignore


class MyQueue:
    """
    This one implements expensive push operation and cheap pop operation.
    Opposite can also be done easily
    """

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def push(self, data: int):
        while self.stack_1.head:
            self.stack_2.push(self.stack_1.pop().data)

        self.stack_1.push(data)

        while self.stack_2.head:
            self.stack_1.push(self.stack_2.pop().data)

        return self

    def pop(self) -> Optional[Node]:
        if self.stack_1.head:
            return self.stack_1.pop()

        print("queue underflow")
        return None


if __name__ == "__main__":
    q = MyQueue()

    for i in range(10):
        q.push(i)

    h = q.pop()

    while h:
        print(h.data, end=" ")
        h = q.pop()

    print()
