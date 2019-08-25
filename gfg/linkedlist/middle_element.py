"""
Given a singly linked list, find middle of the linked list.
Odd Nodes: given linked list is 1->2->3->4->5 then output should be 3.
Even nodes: there would be two middle nodes, we need to print second middle element.
For example, if given linked listis 1->2->3->4->5->6 then output should be 4.
"""
import random
from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


def middle_element(head: Optional[Node]) -> int:
    fast, slow = head, head

    while slow and fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    if slow is not None:
        return slow.data

    return -1


if __name__ == "__main__":
    head = Node(1)
    temp = head

    for i in range(random.randint(5, 10)):
        temp.next = Node(random.randint(10, 10_000))
        temp = temp.next

    temp = head

    print("Linked list")
    while temp.next:
        print(temp.data, end=", ")
        temp = temp.next

    print(temp.data)
    print("middle element:", middle_element(head))
