"""
Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
"""
from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Optional[Node] = None


def kth_last_element(linked_list: Node, k: int) -> Optional[int]:
    """
    Using 2 pointers
    Time complexity: O(n)
    Space Complexity: O(1)
    """
    first_pointer: Optional[Node] = linked_list
    second_pointer: Optional[Node] = linked_list

    while k and first_pointer:
        first_pointer = first_pointer.next
        k -= 1

    while first_pointer and second_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    return second_pointer.data if second_pointer else None


if __name__ == "__main__":
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    print("The 2nd from last element is:", kth_last_element(ll, 2))
