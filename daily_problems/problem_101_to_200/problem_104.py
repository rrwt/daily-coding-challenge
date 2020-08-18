"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""
from typing import Optional


class LLNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class DLLNode(LLNode):
    def __init__(self, data: int) -> None:
        super().__init__(data)
        self.prev = None


def is_palindrome_dll(root_node: DLLNode) -> bool:
    """
    O(n) and O(1)
    """
    tail = root_node

    while tail and tail.next:
        tail = tail.next

    while root_node != tail and root_node.next != tail:
        if root_node.data == tail.data:
            root_node = root_node.next
            tail = tail.prev
        else:
            return False

    # also covers None
    return root_node == tail or root_node.data == tail.data


def is_palindrome_ll(root_node: LLNode) -> bool:
    """
    O(n) and O(n)
    """
    stack = []
    tail = root_node

    while tail and tail.next:
        stack.append(tail)
        tail = tail.next

    while root_node != tail and root_node.next != tail and stack:
        if tail.data != root_node.data:
            return False
        else:
            tail = stack.pop()
            root_node = root_node.next

    return root_node == tail or root_node.data == tail.data


def create_ll(values: list) -> Optional[LLNode]:
    if not values:
        return None

    root = LLNode(values[0])
    tail = root

    for index in range(1, len(values)):
        node = LLNode(values[index])
        tail.next = node
        tail = tail.next

    return root


def create_dll(values: list) -> Optional[DLLNode]:
    if not values:
        return None

    root = DLLNode(values[0])
    tail = root

    for index in range(1, len(values)):
        node = DLLNode(values[index])
        tail.next = node
        node.prev = tail
        tail = tail.next

    return root


if __name__ == "__main__":
    first_dll = create_dll([1, 4, 3, 1, 3, 4, 1])
    first_ll = create_ll([1, 4, 3, 1, 3, 4, 1])
    assert is_palindrome_ll(first_ll) is True
    assert is_palindrome_dll(first_dll) is True

    second_dll = create_dll([1, 4])
    second_ll = create_ll([1, 4])
    assert is_palindrome_ll(second_ll) is False
    assert is_palindrome_dll(second_dll) is False

    third_dll = create_dll([1, 4, 3, 3, 4, 1])
    third_ll = create_ll([1, 4, 3, 3, 4, 1])
    assert is_palindrome_ll(third_ll) is True
    assert is_palindrome_dll(third_dll) is True
