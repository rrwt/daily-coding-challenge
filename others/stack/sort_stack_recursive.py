"""
sort a stack using recursion
"""
from random import randint

from stack import Stack, Node  # type: ignore


def insert_sorted(stack: Stack, node: Node) -> Stack:
    if not stack.head:
        stack.head = node
    else:
        data = node.data

        if data <= stack.peek():
            stack.push(data)
        else:
            temp = stack.pop()
            insert_sorted(stack, node)
            stack.push(temp.data)

    return stack


def sort_stack_recursion(stack: Stack) -> Stack:
    if not stack.head:
        return stack

    temp = stack.pop()
    return insert_sorted(sort_stack_recursion(stack), temp)


if __name__ == "__main__":
    stack = Stack()

    for _ in range(10):
        stack.push(randint(10, 10000))

    h = stack.head

    if h:
        while h.next:
            print(h.data, end=" ")
            h = h.next
        print(h.data)

    stack = sort_stack_recursion(stack)

    h = stack.head

    if h:
        while h.next:
            print(h.data, end=" ")
            h = h.next
        print(h.data)
