"""
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out)
data structure with the following methods: enqueue, which inserts an element into the
queue, and dequeue, which removes it.
"""


class Queue:
    """Queue using 2 stacks
    Enqueue: O(1)
    Deque: O(n)
    """

    def __init__(self):
        self.stack_1: list = []
        self.stack_2: list = []

    def enqueue(self, data: int) -> None:
        self.stack_1.append(data)

    def dequeue(self) -> int:
        if not (self.stack_1 or self.stack_2):
            raise Exception("Queue Underflow")

        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()


if __name__ == "__main__":
    q: Queue = Queue()

    for i in range(1, 10):
        q.enqueue(i)

    for _ in range(9):
        print(q.dequeue())
