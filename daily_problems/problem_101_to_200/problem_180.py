"""
Given a stack of N elements, interleave the first half of the stack
with the second half reversed using only one other queue.
This should be done in-place.
Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example,
    if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
    If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
"""
from collections import deque
from typing import List


class Stack:
    def __init__(self) -> None:
        self._stack = []
        self._size = 0

    def push(self, data: int) -> None:
        self._stack.append(data)
        self._size += 1

    def pop(self) -> int:
        if self._size <= 0:
            raise Exception("Stack Underflow")
        self._size -= 1
        return self._stack.pop()

    @property
    def size(self) -> int:
        return self._size

    @property
    def stack(self) -> List[int]:
        return self._stack


class Queue:
    def __init__(self) -> None:
        self._queue = deque()
        self._size = 0

    def enqueue(self, data: int) -> None:
        self._queue.append(data)
        self._size += 1

    def dequeue(self) -> int:
        if self._size <= 0:
            raise Exception("Queue Underflow")
        self._size -= 1
        return self._queue.popleft()

    @property
    def size(self):
        return self._size


def interleave_stack(stack: Stack) -> Stack:
    count_sec = stack.size // 2
    queue = Queue()

    for _ in range(count_sec):
        queue.enqueue(stack.pop())

    if stack.size == queue.size:  # even
        for _ in range(queue.size - 1):
            queue.enqueue(queue.dequeue())

    while stack.size > 1:
        # interleave in queue
        queue.enqueue(stack.pop())

        for _ in range(queue.size - 2):
            queue.enqueue(queue.dequeue())

    while queue.size > 0:
        stack.push(queue.dequeue())

    return stack


if __name__ == "__main__":
    for num_el in range(1, 10):
        s = Stack()

        for _ in range(1, num_el + 1):
            s.push(_)

        print(s.stack)

        t = interleave_stack(s)
        print(t.stack)
