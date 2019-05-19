"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous
stack exceeds some threshold. Implement a data structure SetOfStacks that mimics
this. SetOfStacks should be composed of several stacks and should create a new
stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.
pop() should behave identically to a single stack (that is, pop() should return
the same values as it would if there were just a single stack).
"""
from __future__ import annotations
from typing import Optional
from random import randint

from stack import Node  # type: ignore


# TODO: implement pop_at(index) to pop element on a specific substack
class SetOfStacks:
    def __init__(
        self, head: Node = None, number_of_stacks: int = 3, stack_size: int = 3
    ):
        self.head: list = [head] + [None] * (number_of_stacks - 1)
        self.number_of_stacks: int = number_of_stacks
        self.stack_size: int = stack_size
        self.count_current: int = 1 if head else 0
        self.current_stack: int = number_of_stacks - 1

    def push(self, data: int) -> Optional[SetOfStacks]:
        print(data, end=" ")
        if self.count_current == self.stack_size:
            if self.current_stack == 0:
                print("Stack Overflow")
                return None
            else:
                self.count_current = 1
                self.current_stack -= 1
                self.head[self.current_stack] = Node(data)
        else:
            node: Node = Node(data)

            if self.head[self.current_stack]:
                node.next = self.head[self.current_stack]

            self.head[self.current_stack] = node
            self.count_current += 1

        return self

    def pop(self) -> Optional[Node]:
        if self.count_current == 0:
            print("stack underflow")
            return None
        else:
            head: Node = self.head[self.current_stack]
            self.head[self.current_stack] = head.next if head else None

            if self.count_current == 1:
                if self.current_stack == self.number_of_stacks - 1:
                    self.count_current = 0
                else:
                    self.count_current = self.stack_size
                    self.current_stack += 1
            else:
                self.count_current -= 1

            return head


if __name__ == "__main__":
    sos = SetOfStacks()

    for i in range(10):
        sos.push(randint(0, 1000))

    for i in range(10):
        node: Node = sos.pop()
        if node:
            print(node.data, end=" ")
    print()
