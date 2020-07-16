"""
Delete k array elements which are smaller than next or become smaller
e.g. input: [20, 10, 25, 30, 40], k = 2
     output: [25 30 40]
"""
from collections import deque

from gfg.stack.stack import Stack  # type: ignore


def delete_smaller(elements: deque, k: int) -> deque:
    """
    It's easier to use a stack to resolve this problem because of problem's
    nature of changing comparision
    """
    stack = Stack()
    stack.push(elements.popleft())

    while elements and k > 0:
        while k > 0 and stack.head and stack.peek() < elements[0]:
            stack.pop()
            k -= 1
        stack.push(elements.popleft())

    while stack.head:
        elements.appendleft(stack.pop().data)

    return elements


if __name__ == "__main__":
    print(delete_smaller(deque([20, 10, 25, 30, 40]), 2))
