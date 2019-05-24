"""
Reverse a stack using recursion
"""
from typing import Optional

from stack import Stack, Node  # typing: ignore


def insert_reversed_node(stack: Stack, node: Node) -> Stack:
    """
    Prepend a node to stack.
    Time complexity: O(n)
    Space complexity: O(n)  # stack
    """
    if not stack.head:
        stack.head = node
        return stack
    else:
        temp = stack.pop()
        insert_reversed_node(stack, node)
        stack.push(temp.data)
        return stack


def reverse_stack_recursive(stack: Stack) -> Stack:
    """
    Time complexity: O(n*n)
    Space complexity: O(n*n)  # recursion stack
    """
    if not stack.head:
        return stack

    temp = stack.pop()
    new_stack = reverse_stack_recursive(stack)

    return insert_reversed_node(new_stack, temp)


if __name__ == "__main__":
    stack = Stack()
    stack.push(5).push(4).push(3).push(2).push(1)
    h = stack.head

    if h:
        while h.next:
            print(h.data, end="->")
            h = h.next
        print(h.data)

    stack = reverse_stack_recursive(stack)
    h = stack.head

    if h:
        while h and h.next:
            print(h.data, end="->")
            h = h.next
        print(h.data)
