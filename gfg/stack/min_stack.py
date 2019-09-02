"""
Design a Data Structure SpecialStack that supports all the stack operations
like push(), pop(), isEmpty(), isFull() and an additional operation getMin()
which should return minimum element from the SpecialStack. All these operations
of SpecialStack must be O(1). To implement SpecialStack, you should only use
standard Stack data structure and no other data structure like arrays, list, .. etc.
"""


class Stack:
    """
    We can store data in 2 stacks
    1. normal stack
    2. min stack with min value of the stack at the top
    """

    def __init__(self, max_size: int):
        self.stack: list = []
        self.min_stack: list = []
        self.size = 0
        self.max_size = max_size

    def push(self, value: int):
        if self.is_empty():
            self.min_stack.append(value)
        elif self.is_full():
            raise MemoryError("Stack is full")
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))

        self.stack.append(value)
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise AssertionError("Stack is Empty")
        else:
            self.min_stack.pop()
            self.size -= 1
            return self.stack.pop()

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def get_min(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    s = Stack(5)
    s.push(30)
    print(s.get_min())
    s.push(20)
    print(s.get_min())
    s.push(40)
    print(s.get_min())
    s.push(10)
    print(s.get_min())
    s.push(50)
    print(s.get_min())
    s.pop()
    print(s.get_min())
    s.pop()
    print(s.get_min())
    s.pop()
    print(s.get_min())
    s.pop()
    print(s.get_min())
