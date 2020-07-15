"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack.
    If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently.
    If there are no elements in the stack, then it should throw an error or return null.
"""
from random import randint
from typing import Optional


class Stack:
    def __init__(self) -> None:
        self.stack: list = []
        self._max_stack: list = []

    def pop(self) -> Optional[int]:
        if self.stack:
            self._max_stack.pop()
            return self.stack.pop()
        return None

    def push(self, value: int) -> None:
        self.stack.append(value)

        if self._max_stack:
            if self._max_stack[-1] < value:
                self._max_stack.append(value)
            else:
                self._max_stack.append(self._max_stack[-1])
        else:
            self._max_stack.append(value)

    def max(self) -> Optional[int]:
        if self._max_stack:
            return self._max_stack[-1]
        return None


if __name__ == "__main__":
    s: Stack = Stack()

    for i in range(1, 10):
        s.push(randint(1, 100))

    print(s.stack)
    print(s.max())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.max())
