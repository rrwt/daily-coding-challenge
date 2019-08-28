"""
You are given a Double Link List with one pointer of each node pointing to the next node
just like in a single link list. The second pointer however can point to any node in the
list and not just the previous node. Now write a program in O(n) time to duplicate this list.
That is, write a program which will create a copy of this list.
Let us call the second pointer as arbit pointer as it can point
to any arbitrary node in the linked list.
"""
from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.arbitrary: Optional[Node] = None
        self.next: Optional[Node] = None


def clone(head: Optional[Node]) -> Optional[Node]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return None

    temp: Optional[Node] = head

    while temp:
        next_temp = temp.next
        new_temp = Node(temp.data)
        temp.next, new_temp.next = new_temp, next_temp
        new_temp.arbitrary = temp.arbitrary
        temp = new_temp.next

    temp = head.next

    while temp and temp.arbitrary:
        temp.arbitrary = temp.arbitrary.next

        if temp.next:
            temp = temp.next.next
        else:
            break

    temp = head
    new_head = temp.next

    while temp and temp.next:
        temp.next = temp.next.next
        temp = temp.next

    return new_head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.arbitrary = head.next.next
    head.next.arbitrary = head
    head.next.next.arbitrary = head.next.next.next.next
    head.next.next.next.arbitrary = head.next.next
    head.next.next.next.next.arbitrary = head.next

    new_head = clone(head)

    while new_head:
        print(new_head.data, end=" ")
        new_head = new_head.next
    print()

    while head:
        print(head.data, end=" ")
        head = head.next
    print()
