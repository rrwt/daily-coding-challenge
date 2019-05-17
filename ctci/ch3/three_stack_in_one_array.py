"""
Describe how you could use a single array to implement three stacks.
"""
from typing import Optional
from random import randint
from array import array

from stack import Stack, Node  # type: ignore


class MultiStackArray:
    def __init__(self, number_of_stacks: int, size: int):
        if number_of_stacks > size:
            raise Exception('Number of stacks cannot exceed the array size')

        self.array: array = array('b', [-1]*size)
        self.size = size
        self.number_of_stacks = number_of_stacks
        self.top_of_stack: array = array('b', [-1]*number_of_stacks)
        self.next_slot: array = array('b', [i+1 for i in range(size)])
        self.next_slot[-1] = -1  # stack is full
        self.pointer: int = 0  # next empty slot

    def push(self, stack_num: int, data: int):
        if self.pointer == -1:
            raise ValueError('stack overflow')

        slot: int = self.pointer
        self.array[slot] = data
        self.pointer = self.next_slot[slot]
        self.next_slot[slot] = self.top_of_stack[stack_num]
        self.top_of_stack[stack_num] = slot

    def pop(self, stack_num: int) -> Optional[int]:
        if self.top_of_stack[stack_num] == -1:
            print('stack underflow')
            return None

        tos: int = self.top_of_stack[stack_num]
        self.top_of_stack[stack_num] = self.next_slot[tos]
        self.next_slot[tos] = self.pointer
        self.pointer = tos

        return self.array[tos]


if __name__ == "__main__":
    msa = MultiStackArray(3, 10)

    for i in range(10):
        msa.push(randint(0, 2), i)
