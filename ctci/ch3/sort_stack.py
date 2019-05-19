"""
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure (such as an array). The stack supports the
following operations: push, pop, peek, and isEmpty.
"""
from stack import Stack, Node  # type: ignore


class SortStack(Stack):
    def sort(self):
        buffer: Stack = Stack()

        while self.head.next:
            buffer.push(self.pop().data)

        while buffer.head:
            data: int = buffer.pop().data

            while self.head and self.head.data < data:
                buffer.push(self.pop().data)

            self.push(data)


if __name__ == "__main__":
    ss = SortStack()

    from random import randint

    for i in range(10):
        ss.push(randint(1, 1000))

    head = ss.head

    print("Original Data", end=": ")
    while head.next:
        print(head.data, end="->")
        head = head.next
    print(head.data)

    ss.sort()
    head = ss.head

    print("Sorted Data", end=": ")
    while head.next:
        print(head.data, end="->")
        head = head.next
    print(head.data)
