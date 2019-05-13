"""
We are given a stack data structure with push and pop operations,
the task is to implement a queue using instances of stack data
structure and operations on them.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)

        if self.head:
            node.next = self.head

        self.head = node

    def pop(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp.data
        else:
            print('stack underflow')
            raise ValueError('Stack UnderFlow')


class Queue:
    """
    A queue can be implemented using 2 stacks.
    This implementation is O(1) push and O(n) pop.
    Alternatively O(n) push and O(1) pop can also be implemented
    """

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def push(self, data):
        self.stack_1.push(data)

    def pop(self):
        while self.stack_1.head:
            self.stack_2.push(self.stack_1.pop())

        self.stack_1 = Stack()
        data = self.stack_2.pop()

        while self.stack_2.head:
            self.stack_1.push(self.stack_2.pop())

        self.stack_2 = Stack()
        return data


if __name__ == '__main__':
    q = Queue()

    q.push(1)
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    assert q.pop() == 2

    q.push(4)
    assert q.pop() == 3
