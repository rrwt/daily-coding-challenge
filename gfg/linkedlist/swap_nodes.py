"""
Given a linked list and two keys in it, swap nodes for two given keys.
Nodes should be swapped by changing links. Swapping data of nodes may
be expensive in many situations when data contains many fields.
It may be assumed that all keys in linked list are distinct.
"""
from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Node] = None


def swap_nodes(head: Optional[Node], x: int, y: int) -> Optional[Node]:
    """
    Cases:
        1. Adjacent
        2. One of them is at the end/beginning
        3. One of them is not present
    """

    prev_1, node_1, prev_2, node_2 = None, None, None, None
    temp = head

    while temp is not None:
        if temp.data in (x, y):
            node_1 = temp
            prev_2 = temp
            temp = temp.next
            break
        else:
            prev_1 = temp
            temp = temp.next

    while temp is not None:
        if temp.data in (x, y):
            node_2 = temp
            break
        else:
            prev_2 = temp
            temp = temp.next

    if node_1 and node_2 and prev_2:
        if node_1.next == node_2:
            if prev_1 is None:
                node_1.next = node_2.next
                node_2.next = node_1
                head = node_2
            else:
                prev_1.next = node_2
                node_1.next = node_2.next
                node_2.next = node_1
        elif prev_1 is None:
            prev_2.next = node_1
            temp = node_1.next
            node_1.next = node_2.next
            node_2.next = temp
            head = node_2
        else:
            prev_1.next, prev_2.next, node_1.next, node_2.next = (
                node_2,
                node_1,
                node_2.next,
                node_1.next,
            )
    else:
        raise AssertionError("One of the node wasn't found")

    return head


def print_ll(head: Optional[Node]) -> None:
    temp = head

    while temp and temp.next:
        print(temp.data, end="->")
        temp = temp.next
    if temp:
        print(temp.data)


if __name__ == "__main__":
    head: Optional[Node] = Node(1)
    temp = head

    for i in range(2, 8):
        if temp:
            temp.next = Node(i)
            temp = temp.next

    print("Original List:")
    print_ll(head)
    print("List after exchanging 4 with 3")
    head = swap_nodes(head, 4, 3)
    print_ll(head)
    print("List after exchanging 1 with 7")
    head = swap_nodes(head, 1, 7)
    print_ll(head)
    print("List after exchanging 1 with 6")
    head = swap_nodes(head, 1, 6)
    print_ll(head)
    print("List after exchanging 7 with 2")
    head = swap_nodes(head, 2, 7)
    print_ll(head)
