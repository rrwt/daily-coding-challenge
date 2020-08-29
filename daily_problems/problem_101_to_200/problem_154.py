"""
Implement a stack API using only a heap. A stack implements the following methods:
    push(item), which adds an element to the stack
    pop(), which removes and returns the most recently added
    element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:
    push(item), which adds a new key to the heap
    pop(), which removes and returns the max value of the heap
"""
import heapq
import sys


class Stack:
    def __init__(self):
        # min heap
        self.heap = []
        heapq.heapify(self.heap)
        self.count = sys.maxsize

    def push(self, item) -> None:
        heapq.heappush(self.heap, (self.count, item))
        self.count -= 1

    def pop(self) -> int:
        if self.count == sys.maxsize:
            raise ValueError("Cannot pop empty stack")

        value = heapq.heappop(self.heap)
        self.count += 1
        return value[1]


if __name__ == "__main__":
    s = Stack()

    for i in range(10):
        s.push(i)

    for i in range(9, -1, -1):
        assert s.pop() == i

    try:
        s.pop()
    except ValueError:
        print("success")
