"""
We are given queue data structure, the task is to
implement stack using only given queue data structure.
"""
from collections import deque
from typing import Optional


class StackUsingQueue:
    """
    The solution using 2 queues is trivial and similar to queue using 2 stacks.
    The modified version of the solution would be to keep count of number of elements
    in the queue after every push and pop operation. After every push operation,
    we deque all but last element and enque them again.
    Insertion: O(n)
    Deletion: O(1)
    """

    def __init__(self):
        self.queue = deque()
        self.count: int = 0

    def push(self, data: int):
        self.queue.append(data)

        for _ in range(self.count):
            self.queue.append(self.queue.popleft())

        self.count += 1

    def pop(self) -> Optional[int]:
        if self.count:
            self.count -= 1
            return self.queue.popleft()

        return None
