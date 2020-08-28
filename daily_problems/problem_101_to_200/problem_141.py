"""
Implement 3 stacks using a single list
"""
from random import randint


class Stack:
    def __init__(self):
        self.list = []
        self.size = 0  # count of number of max possible elements in stack
        self.indexes = [-1, -1, -1]  # store last indexes of stacks i.e. top of stack
        self.next_index = 0  # next empty index in list or size of list
        self.prev_indexes = []  # link to previous stack elements for all 3 stacks

    def pop(self, stack_number) -> int:
        if self.indexes[stack_number] < 0:
            raise ValueError("Stack underflow")

        index = self.indexes[stack_number]
        val = self.list[index]
        self.indexes[stack_number] = self.prev_indexes[index]

        if index == self.size - 1:
            self.list.pop()
            self.prev_indexes.pop()
            self.size -= 1

            if self.next_index > self.size:
                self.next_index -= 1
        else:
            self.list[index] = None
            self.prev_indexes[index] = -1

            if index < self.next_index:
                self.next_index = index

        return val

    def push(self, item, stack_number) -> None:
        if self.next_index < self.size:
            self.prev_indexes[self.next_index] = self.indexes[stack_number]
            self.indexes[self.next_index] = item
        else:
            self.list.append(item)
            self.size += 1
            self.prev_indexes.append(self.indexes[stack_number])

        self.indexes[stack_number] = self.next_index
        self.set_next_index()

    def set_next_index(self) -> None:
        for index in range(self.next_index, self.size):
            if self.list[index] is None:
                self.next_index = index
                return None

        self.next_index = self.size

    def print_stack(self, stack_number: int) -> None:
        index = self.indexes[stack_number]
        print(self.list[index], end=" ")

        while (index := self.prev_indexes[index]) > -1:
            print(self.list[index], end=" ")

        print()


if __name__ == "__main__":
    stack = Stack()

    for _ in range(randint(10, 20)):
        s_n = randint(0, 2)
        val = randint(0, 30)
        print(f"pushing {val} to stack {s_n}")
        stack.push(val, s_n)

    print("stack 0:")
    stack.print_stack(0)
    print("stack 1:")
    stack.print_stack(1)
    print("stack 2:")
    stack.print_stack(2)

    for s_n in range(3):
        print(f"stack {s_n}:")
        for _ in range(10):
            try:
                print(stack.pop(s_n), end=" ")
            except ValueError:
                pass
        print()
